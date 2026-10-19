/**
 * Per-tab session state.
 *
 * Extracted from BrowserManager to enable parallel tab execution in /batch.
 * Each TabSession holds the state that is scoped to a single browser tab:
 * page reference, element refs, snapshot baseline, and frame context.
 *
 *   BrowserManager (global)
 *     â””â”€â”€ tabSessions: Map<number, TabSession>
 *           â”œâ”€â”€ TabSession(page1)  â†  refMap, lastSnapshot, frame
 *           â”œâ”€â”€ TabSession(page2)  â†  refMap, lastSnapshot, frame
 *           â””â”€â”€ TabSession(page3)  â†  refMap, lastSnapshot, frame
 *
 * The /command path gets the active session via bm.getActiveSession().
 * The /batch path gets specific sessions via bm.getSession(tabId).
 * Both paths pass TabSession to the same handler functions.
 */

import type { Page, Locator, Frame } from 'playwright';

export interface RefEntry {
  locator: Locator;
  role: string;
  name: string;
}

export type SetContentWaitUntil = 'load' | 'domcontentloaded' | 'networkidle';

export class TabSession {
  readonly page: Page;

  // â”€â”€â”€ Ref Map (snapshot â†’ @e1, @e2, @c1, @c2, ...) â”€â”€â”€â”€â”€â”€â”€â”€
  private refMap: Map<string, RefEntry> = new Map();

  // â”€â”€â”€ Snapshot Diffing â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
  // NOT cleared on navigation â€” it's a text baseline for diffing
  private lastSnapshot: string | null = null;

  // â”€â”€â”€ Frame context â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
  private activeFrame: Frame | null = null;

  // â”€â”€â”€ Loaded HTML (for load-html replay across context recreation) â”€
  //
  // loadedHtml lifecycle:
  //
  //   load-html cmd â”€â”€â–¶ session.setTabContent(html, opts)
  //                          â”œâ”€â–¶ page.setContent(html, opts)
  //                          â””â”€â–¶ this.loadedHtml = html
  //                              this.loadedHtmlWaitUntil = opts.waitUntil
  //
  //   goto/back/forward/reload â”€â”€â–¶ session.clearLoadedHtml()
  //                                     (BEFORE Playwright call, so timeouts
  //                                      don't leave stale state)
  //
  //   viewport --scale â”€â”€â–¶ recreateContext()
  //                             â”œâ”€â–¶ saveState() captures { url, loadedHtml } per tab
  //                             â”‚        (in-memory only, never to disk)
  //                             â””â”€â–¶ restoreState():
  //                                    for each tab with loadedHtml:
  //                                       newSession.setTabContent(html, opts)
  //                                    (NOT page.setContent â€” must rehydrate
  //                                     TabSession.loadedHtml too)
  private loadedHtml: string | null = null;
  private loadedHtmlWaitUntil: SetContentWaitUntil | undefined;

  constructor(page: Page) {
    this.page = page;
  }

  // â”€â”€â”€ Page Access â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
  getPage(): Page {
    return this.page;
  }

  // â”€â”€â”€ Ref Map â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
  setRefMap(refs: Map<string, RefEntry>) {
    this.refMap = refs;
  }

  clearRefs() {
    this.refMap.clear();
  }

  /**
   * Resolve a selector that may be a @ref (e.g., "@e3", "@c1") or a CSS selector.
   * Returns { locator } for refs or { selector } for CSS selectors.
   */
  async resolveRef(selector: string): Promise<{ locator: Locator } | { selector: string }> {
    if (selector.startsWith('@e') || selector.startsWith('@c')) {
      const ref = selector.slice(1); // "e3" or "c1"
      const entry = this.refMap.get(ref);
      if (!entry) {
        throw new Error(
          `Ref ${selector} not found. Run 'snapshot' to get fresh refs.`
        );
      }
      const count = await entry.locator.count();
      if (count === 0) {
        throw new Error(
          `Ref ${selector} (${entry.role} "${entry.name}") is stale â€” element no longer exists. ` +
          `Run 'snapshot' for fresh refs.`
        );
      }
      return { locator: entry.locator };
    }
    return { selector };
  }

  /** Get the ARIA role for a ref selector, or null for CSS selectors / unknown refs. */
  getRefRole(selector: string): string | null {
    if (selector.startsWith('@e') || selector.startsWith('@c')) {
      const entry = this.refMap.get(selector.slice(1));
      return entry?.role ?? null;
    }
    return null;
  }

  getRefCount(): number {
    return this.refMap.size;
  }

  /** Get all ref entries for the /refs endpoint. */
  getRefEntries(): Array<{ ref: string; role: string; name: string }> {
    return Array.from(this.refMap.entries()).map(([ref, entry]) => ({
      ref, role: entry.role, name: entry.name,
    }));
  }

  // â”€â”€â”€ Snapshot Diffing â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
  setLastSnapshot(text: string | null) {
    this.lastSnapshot = text;
  }

  getLastSnapshot(): string | null {
    return this.lastSnapshot;
  }

  // â”€â”€â”€ Frame context â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
  setFrame(frame: Frame | null): void {
    this.activeFrame = frame;
  }

  getFrame(): Frame | null {
    return this.activeFrame;
  }

  /**
   * Returns the active frame if set, otherwise the current page.
   * Use this for operations that work on both Page and Frame (locator, evaluate, etc.).
   */
  getActiveFrameOrPage(): Page | Frame {
    // Auto-recover from detached frames (iframe removed/navigated). Clear
    // refs alongside the activeFrame â€” same staleness condition as
    // onMainFrameNavigated() below: refs were captured against a frame
    // that no longer exists. Without this, refMap entries linger against
    // a dead frame after silently falling back to the main page; the
    // next snapshot's role+name keys collide with stale entries and the
    // resolver picks one at random.
    if (this.activeFrame?.isDetached()) {
      this.activeFrame = null;
      this.clearRefs();
    }
    return this.activeFrame ?? this.page;
  }

  /**
   * Called on main-frame navigation to clear stale refs, frame context, and any
   * load-html replay metadata. Runs for every main-frame nav â€” explicit goto/back/
   * forward/reload AND browser-emitted navigations (link clicks, form submits, JS
   * redirects, OAuth). Without clearing loadedHtml here, a user who load-html'd and
   * then clicked a link would silently revert to the original HTML on the next
   * viewport --scale.
   */
  onMainFrameNavigated(): void {
    this.clearRefs();
    this.activeFrame = null;
    this.loadedHtml = null;
    this.loadedHtmlWaitUntil = undefined;
  }

  // â”€â”€â”€ Loaded HTML (load-html replay) â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

  /**
   * Load HTML content into the tab AND store it for replay after context recreation
   * (e.g. viewport --scale). Unlike page.setContent() alone, this rehydrates
   * TabSession.loadedHtml so the next saveState()/restoreState() round-trip preserves
   * the content.
   */
  async setTabContent(html: string, opts: { waitUntil?: SetContentWaitUntil } = {}): Promise<void> {
    const waitUntil = opts.waitUntil ?? 'domcontentloaded';
    // Call setContent FIRST â€” only record the replay metadata after a successful load.
    // If setContent throws (timeout, crash), we must not leave phantom HTML that a
    // later viewport --scale would replay.
    await this.page.setContent(html, { waitUntil, timeout: 15000 });
    this.loadedHtml = html;
    this.loadedHtmlWaitUntil = waitUntil;
  }

  /** Get stored HTML + waitUntil for state replay. Returns null if no load-html happened. */
  getLoadedHtml(): { html: string; waitUntil?: SetContentWaitUntil } | null {
    if (this.loadedHtml === null) return null;
    return { html: this.loadedHtml, waitUntil: this.loadedHtmlWaitUntil };
  }

  /** Clear stored HTML. Called BEFORE goto/back/forward/reload navigation. */
  clearLoadedHtml(): void {
    this.loadedHtml = null;
    this.loadedHtmlWaitUntil = undefined;
  }
}
