
# NIGD Common Data Matrix

Use this when the organization needs a clear view of which roles are accountable for common data domains. The output is a domain-by-role matrix.

## Artifact

Produce a Common Data Matrix with:

1. **Rows: data domains** - customer, product, finance, employee, donor, shipment, inventory, or other shared subject areas.
2. **Columns: governance roles** - operational steward, domain steward, coordinator, executive sponsor, IT/data partner, privacy/security partner, and major consumer groups.
3. **Cells: accountability facts** - person/team, decision rights, key systems, key definitions, data issues, and involvement trigger.
4. **Gap markers** - unowned domains, duplicate ownership, conflicting definitions, missing consumers, and missing escalation paths.
5. **Action plan** - the first domains to formalize and the conversations needed to fill blank or contested cells.

## Process

1. Define data domains at a business level. Avoid rows for applications, tables, reports, or pipeline stages unless they represent a true business subject area.
2. Associate roles before names when needed. The matrix can start with accountable roles and later fill in people.
3. Fill cells with evidence from existing work: process ownership, data issue resolution, reporting ownership, regulatory responsibility, or subject-matter expertise.
4. Highlight conflicts instead of smoothing them over. Multiple stewards can exist for one data type, but their relationship must be explicit.
5. Use the matrix as a conversation tool. The goal is not a perfect spreadsheet; it is agreement on accountability.

## Failure Modes

- **Application inventory drift** - turning the matrix into a system catalog rather than a common-data accountability map.
- **Blank-cell avoidance** - hiding unknown ownership instead of using gaps to drive governance conversations.
- **Single-steward myth** - forcing one owner for a domain where multiple stewards govern different definitions, processes, or uses.
- **No decision rights** - listing names without clarifying what each person can decide or approve.
- **Matrix shelfware** - creating the matrix once and never connecting it to issue triage, projects, or policy work.

## Output Format

Return the matrix, top accountability gaps, contested domains, and recommended follow-up interviews or workshops.

## References

- Robert S. Seiner, *Non-Invasive Data Governance* (Technics Publications, 2014), Chapter 11.
- Sibling skills: `nigd-stewardship-accountability-matrix`, `nigd-activity-matrix`.
