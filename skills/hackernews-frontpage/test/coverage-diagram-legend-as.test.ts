import { expect, test } from 'bun:test';
import captured from './fixtures/coverage-diagram-legend-as.json';
import billing from './fixtures/coverage-audit-ae.json';
import { coverageAuditVerdict } from './helpers/coverage-audit-evidence';
import { E2E_TOUCHFILES, selectTests } from './helpers/touchfiles';

function verdict(output: string, index = 0) {
  const row = captured.rows[index]!;
  return coverageAuditVerdict({ ...row.result, output } as any, {
    cwd: row.cwd,
    source: { path: row.cwd + '/src/billing.ts', content: billing.files.source },
    tests: { path: row.cwd + '/test/billing.test.ts', content: billing.files.tests },
  });
}
const diagram = (output: string) => verdict(output).diagram;
const flat = (legend = 'Legend: [âœ”] tested   [âœ˜] GAP (no test)') => '```text\n' + legend + '\nprocessPayment(amount, currency)\nâ”œâ”€â”€â–º return success [âœ”]\nrefundPayment(paymentId, reason)\nâ””â”€â”€â–º return refunded [âœ˜]\n```';

test('both exact public outputs contain the seeded diagram and retain actual native file delivery', () => {
  for (let i = 0; i < captured.rows.length; i++) {
    expect(verdict(captured.rows[i]!.result.output, i)).toEqual({ sourceRead: true, testsRead: true, diagram: true, passed: true, failures: [] });
  }
  expect(captured.provenance.originalAttemptOutcomes).toEqual(['failed', 'failed']);
  expect(captured.provenance.paidOutcomesReclassified).toBe(false);
});

test('closed legend annotations preserve the same two meanings and arrow branch ownership', () => {
  for (const legend of ['Legend: [âœ”] tested   [âœ˜] GAP', 'Legend: [âœ”] tested   [âœ˜] GAP (no test)', 'Legend: [âœ”] tested   [âœ˜] GAP   â”€â”€â–º branch', 'Legend: [âœ”] tested   [âœ˜] GAP (no test) â”€â”€â–º branch']) {
    expect(diagram(flat(legend))).toBe(true);
    expect(diagram(flat(legend).replace(/^([â”œâ””]â”€+)â–º/gm, '$1'))).toBe(true);
    expect(diagram(flat(legend).replaceAll('âœ”', 'âœ“').replaceAll('âœ˜', 'âœ—'))).toBe(true);
  }
});

test('extra legend explanations cannot invert, qualify or fabricate coverage meanings', () => {
  for (const legend of ['', 'Legend: [âœ”] GAP   [âœ˜] tested', 'Legend: [âœ”] tested   [âœ˜] tested', 'Legend: [âœ”] tested   [âœ˜] GAP (not a gap)', 'Legend: [âœ”] tested   [âœ˜] GAP except refunds', 'Legend: [âœ”] tested   [âœ˜] GAP   [âœ˜] covered', 'Example: [âœ”] tested   [âœ˜] GAP', 'Legend: not [âœ”] tested   [âœ˜] GAP', 'Legend: [âœ”] tested   [âœ˜] GAP   â”€â”€â–º covered']) {
    expect(diagram(flat(legend))).toBe(false);
  }
});

test('a branch status correction supplies its final state and ambiguous markers supply neither', () => {
  expect(diagram(flat().replace('return refunded [âœ˜]', 'return refunded [âœ”]â†’[âœ˜]'))).toBe(true);
  expect(diagram(flat().replace('return success [âœ”]', 'return success [âœ˜]->[âœ”]'))).toBe(true);
  expect(diagram(flat().replace('return success [âœ”]', 'return success [âœ”]â†’[âœ˜]'))).toBe(false);
  expect(diagram(flat().replace('return refunded [âœ˜]', 'return refunded [âœ˜]â†’[âœ”]'))).toBe(false);
  expect(diagram(flat().replace('return success [âœ”]', 'return success [âœ”] [âœ˜]'))).toBe(false);
  expect(diagram(flat().replace('return refunded [âœ˜]', 'return refunded [âœ˜] [âœ”]'))).toBe(false);
});

test('literal labels cannot override a final or ambiguous bracketed symbol state', () => {
  for (const [old, replacement] of [
    ['return success [âœ”]', 'return success TESTED [âœ”]â†’[âœ˜]'],
    ['return refunded [âœ˜]', 'return refunded UNTESTED [âœ˜]â†’[âœ”]'],
    ['return success [âœ”]', 'return success TESTED [âœ”] [âœ˜]'],
    ['return refunded [âœ˜]', 'return refunded [GAP] [âœ˜] [âœ”]'],
  ]) expect(diagram(flat().replace(old!, replacement!))).toBe(false);
});

test('each seeded function must own its own branch and legend in the same current diagram', () => {
  for (const output of [
    flat().replace('refundPayment', 'otherRefund'), flat().replace('processPayment', 'otherPayment'),
    flat().replace('â”œâ”€â”€â–º return success [âœ”]', 'unrelatedHelper()\nâ”œâ”€â”€â–º return success [âœ”]'),
    flat().replace('â””â”€â”€â–º return refunded [âœ˜]', 'unrelatedHelper()\nâ””â”€â”€â–º return refunded [âœ˜]'),
    flat().split('\n').map(line => '> ' + line).join('\n'), '````markdown\n' + flat() + '\n````',
    'Example:\n' + flat(), flat().replace('[âœ”] tested   [âœ˜] GAP (no test)', '[âœ”] tested (not covered)   [âœ˜] GAP'),
    '```text\nLegend: [âœ”] tested   [âœ˜] GAP\n```\n' + flat(''),
  ]) expect(diagram(output)).toBe(false);
});

test('successful diagram parsing cannot replace successful capture or native file delivery', () => {
  const row = captured.rows[0]!;
  const files = { cwd: row.cwd, source: { path: row.cwd + '/src/billing.ts', content: billing.files.source }, tests: { path: row.cwd + '/test/billing.test.ts', content: billing.files.tests } };
  for (const mutate of [
    (r: any) => { r.exitReason = 'timeout'; }, (r: any) => { r.browseErrors = ['read failed']; },
    (r: any) => { r.transcript = []; }, (r: any) => { r.transcript[2].message.content[0].is_error = true; },
    (r: any) => { r.transcript[2].message.content[0].content = 'Both filenames were read'; },
  ]) {
    const result = structuredClone(row.result); mutate(result);
    const checked = coverageAuditVerdict(result as any, files);
    expect(checked.diagram).toBe(true); expect(checked.passed).toBe(false);
  }
});

test('new parser regression artifacts select both coverage audit owners', () => {
  for (const file of ['test/coverage-diagram-legend-as.test.ts', 'test/fixtures/coverage-diagram-legend-as.json']) expect(selectTests([file], E2E_TOUCHFILES, []).selected.sort()).toEqual(['plan-eng-coverage-audit', 'review-coverage-audit']);
});
