# Hardware and platform parity

> **Last reviewed:** 2026-10-10 Â· **Last updated:** 2026-10-11 Â· **Change:** minor (shared print spooler; Windows CI passes) Â· **Target:** Adobe InDesign 2026 (21.6)

What InDesign does with hardware, per platform, against DesignCraft. Layout is not a
GPU-hungry workload, so this dimension carries little weight, but a start that fails on a
graphics driver loses the user entirely. Overall numbers: [target-app-parity.md](target-app-parity.md).

**Hardware: ~45% ready, 20â€“40 h. Platforms: ~55% ready, 40â€“80 h.** (estimated)

## Hardware features

| Feature | InDesign 2026 | DesignCraft macOS | Windows | Linux | Web |
|---|---|---|---|---|---|
| GPU display (canvas) | GPU Performance: GPU preview, animated zoom (Metal on macOS; Windows with supported GPUs) | canvas rasterized on the CPU (vello_cpu, SIMD, multithreaded), presented by wgpu (Metal) | wgpu DirectX 12 (since #297), Vulkan/OpenGL fallback | Vulkan, OpenGL fallback | WebGPU, WebGL2 fallback |
| Start-up on any GPU | robust | Metal device lost on Intel Macs (#334) | AMD OpenGL crash (#167), launch failures (#273) | some reports (#192, #220) | |
| Backend fallback | n/a | `gpu.json` skips a backend whose start never showed a frame (#297) | same | same | |
| Animated / scrubby zoom | âœ“ (GPU) | âœ“ (CPU tiles, damage regions) | âœ“ | âœ“ | âœ“ |
| HiDPI / Retina | âœ“ | âœ“ | âœ“ | âœ“ | âœ“ |
| UI scaling | âœ“ | âœ“ (menus and dialogs usable at larger scales, #281) | âœ“ | âœ“ | âœ“ |
| Multi-monitor, floating document windows | âœ“ | ~ one window; New Window for the same document | ~ | ~ | âœ— |
| Printing | system print with PPDs, PostScript, separations | PDF to CUPS (`craft-print`) | Windows PDF raster spooler (`craft-print`) | PDF to CUPS (`craft-print`) | browser download |
| Colour-managed display (monitor profile) | âœ“ | âœ— (working CMYK profile simulated; monitor profile not applied) | âœ— | âœ— | âœ— |
| Touch / pen | Touch workspace (Windows), gestures | trackpad pinch/scroll | ~ | ~ | ~ |
| Multi-core composition | single-threaded composer per story (documented by Adobe as mostly single-threaded) | parallel story composition (rayon), 6.7Ã— on the sample | âœ“ | âœ“ | single-threaded |

## Platforms

| Platform | InDesign 2026 | DesignCraft | Evidence |
|---|---|---|---|
| macOS (Apple silicon, Intel) | âœ“ | âœ“ primary development platform | Intel GPU start failure (#334); window controls misaligned (#333); font managers (#327) |
| Windows x64 | âœ“ | ~ builds and installers ship | copy/paste and context menus (#351, #312), installer confusion (#64), launch failures (#273, #167) |
| Windows ARM64 | âœ“ | ~ build (CI workflow) | not exercised at runtime |
| Linux (x86_64, aarch64; riscv64 tar.gz) | âœ— | ~ deb, AppImage, Flatpak | clipboard (#164), panels don't scroll (#267), CJK UI font (#332) |
| FreeBSD | âœ— | ~ build | |
| Web (WASM) | âœ— (InDesign on the web is not shipped) | ~ same UI, file picker, downloads; no control channel | |

DesignCraft runs on more platforms than InDesign; what's missing is runtime testing on the ones
the developers don't use daily.

## Remaining effort

| Work | Opus 5.5 h |
|---|---|
| Start-up robustness on every GPU: confirm #297 with reporters, Intel Metal fix, CPU-only present fallback | 15â€“30 |
| Printing fidelity, PostScript and print presets | 15â€“30 (counted in file-format-parity.md) |
| Monitor profile in display colour management | 5â€“10 |
| Windows and Linux runtime smoke tests in CI | 20â€“40 |
| Multi-window document views | 15â€“30 |
| **Hardware + platforms** | **60â€“120** |

## Revision history

| Date | Change | Summary |
|---|---|---|
| 2026-10-10 | major | Created from the code, InDesign 2026's GPU Performance features and the issue tracker |

Windows submission now uses shared craft-print. It selects matching or default driver paper,
shrinks oversized sheets to the printable area without enlarging smaller ones, and preserves
the queue's duplex default; printer-driver options UI and physical output validation remain open.
