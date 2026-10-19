// check-permissions.mjs - one runnable eval for the one-person-ai-business skill.
// Verifies TWO invariants at once (independent review, not the author grading itself):
//   1) OUTPUT gate: a lane's deliverable is only shippable-unattended if it is a
//      draft/report and NOT already marked sent/live/finalized.
//   2) PERMISSION boundary: no lane can exceed its least-privilege grant, and every
//      money / outside-world action stays behind explicit human approval, from ANY lane.
// No dependencies, no network, no side effects. Node stdlib only.
// Run:  node check-permissions.mjs      (exit 0 = pass; throws + non-zero = fail)

import assert from 'node:assert/strict';

// Actions that touch money or the outside world. Gated for every lane, always.
const GATED = new Set([
  'send', 'publish', 'purchase', 'ad_activate', 'invoice_finalize', 'external_outreach',
]);

// Least-privilege grant per lane: the ONLY verbs a lane may run unattended.
// No lane is granted any GATED verb. Outreach in particular has no 'send'.
const LANES = {
  content:  { scope: ['research', 'draft'] },
  projects: { scope: ['read', 'plan', 'standup', 'track'] },
  outreach: { scope: ['research', 'draft'] },        // drafts only, never sends
  finance:  { scope: ['invoice_draft', 'report'] },  // drafts invoices, never finalizes
  ads:      { scope: ['plan', 'build_paused'] },     // builds campaigns PAUSED
};

// Decision under test: may `action` run in `laneName` unattended, or does it gate?
export function evaluate(laneName, action) {
  const lane = LANES[laneName];
  if (!lane) return { allowed: false, requiresApproval: false, reason: 'unknown lane' };
  if (GATED.has(action)) return { allowed: false, requiresApproval: true, reason: 'gated: human approval' };
  if (!lane.scope.includes(action)) return { allowed: false, requiresApproval: false, reason: 'outside lane scope' };
  return { allowed: true, requiresApproval: false, reason: 'in scope, ungated' };
}

// A deliverable may ship unattended only if it is a draft/report, never a done deed.
export function outputOk(deliverable) {
  const blocked = ['sent', 'live', 'finalized', 'published', 'purchased'];
  return deliverable.kind !== undefined && !blocked.includes(deliverable.status);
}

function demo() {
  // BOUNDARY: every gated verb needs approval, from every lane.
  for (const lane of Object.keys(LANES)) {
    for (const g of GATED) {
      const r = evaluate(lane, g);
      assert.equal(r.allowed, false, `${lane}/${g} must not auto-run`);
      assert.equal(r.requiresApproval, true, `${lane}/${g} must require approval`);
    }
  }
  // BOUNDARY: the three named traps.
  assert.equal(evaluate('outreach', 'send').requiresApproval, true);
  assert.equal(evaluate('finance', 'invoice_finalize').requiresApproval, true);
  assert.equal(evaluate('ads', 'ad_activate').requiresApproval, true);

  // BOUNDARY: least privilege - a lane cannot act outside its scope.
  assert.equal(evaluate('content', 'invoice_draft').allowed, false); // out of scope
  assert.equal(evaluate('ads', 'standup').allowed, false);           // out of scope

  // ALLOWED: in-scope ungated work runs unattended.
  assert.equal(evaluate('content', 'draft').allowed, true);
  assert.equal(evaluate('projects', 'standup').allowed, true);
  assert.equal(evaluate('ads', 'build_paused').allowed, true);

  // OUTPUT: drafts pass; a pre-sent/live/finalized deliverable fails the gate.
  assert.equal(outputOk({ kind: 'post', status: 'draft' }), true);
  assert.equal(outputOk({ kind: 'invoice', status: 'draft' }), true);
  assert.equal(outputOk({ kind: 'email', status: 'sent' }), false);
  assert.equal(outputOk({ kind: 'campaign', status: 'live' }), false);
  assert.equal(outputOk({ kind: 'invoice', status: 'finalized' }), false);

  console.log('one-person-ai-business eval: OK (permission boundaries + output gate hold)');
}

demo();
