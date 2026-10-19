---
name: research-grants
description: "Write competitive research proposals for NSF, NIH, DOE, and DARPA. Agency-specific formatting, review criteria, budget preparation, broader impacts, significance statements, innovation narratives, and compliance with submission requirements."
allowed-tools: [Read, Write, Edit, Bash]
---

# Research Grant Writing

## Overview

Research grant writing is the process of developing competitive funding proposals for federal agencies and foundations. Master agency-specific requirements, review criteria, narrative structure, budget preparation, and compliance for NSF (National Science Foundation), NIH (National Institutes of Health), DOE (Department of Energy), and DARPA (Defense Advanced Research Projects Agency) submissions.

**Critical Principle: Grants are persuasive documents that must simultaneously demonstrate scientific rigor, innovation, feasibility, and broader impact.** Each agency has distinct priorities, review criteria, formatting requirements, and strategic goals that must be addressed.

## When to Use This Skill

This skill should be used when:
- Writing research proposals for NSF, NIH, DOE, or DARPA programs
- Preparing project descriptions, specific aims, or technical narratives
- Developing broader impacts or significance statements
- Creating research timelines and milestone plans
- Preparing budget justifications and personnel allocation plans
- Responding to program solicitations or funding announcements
- Addressing reviewer comments in resubmissions
- Planning multi-institutional collaborative proposals
- Writing preliminary data or feasibility sections
- Preparing biosketches, CVs, or facilities descriptions

## Visual Enhancement with Scientific Schematics

**âš ï¸ MANDATORY: Every research grant proposal MUST include at least 1-2 AI-generated figures using the scientific-schematics skill.**

This is not optional. Grant proposals without visual elements are incomplete and less competitive. Before finalizing any document:
1. Generate at minimum ONE schematic or diagram (e.g., project timeline, methodology flowchart, or conceptual framework)
2. Prefer 2-3 figures for comprehensive proposals (research workflow, Gantt chart, preliminary data visualization)

**How to generate figures:**
- Use the **scientific-schematics** skill to generate AI-powered publication-quality diagrams
- Simply describe your desired diagram in natural language
- Nano Banana Pro will automatically generate, review, and refine the schematic

**How to generate schematics:**
```bash
python scripts/generate_schematic.py "your diagram description" -o figures/output.png
```

The AI will automatically:
- Create publication-quality images with proper formatting
- Review and refine through multiple iterations
- Ensure accessibility (colorblind-friendly, high contrast)
- Save outputs in the figures/ directory

**When to add schematics:**
- Research methodology and workflow diagrams
- Project timeline Gantt charts
- Conceptual framework illustrations
- System architecture diagrams (for technical proposals)
- Experimental design flowcharts
- Broader impacts activity diagrams
- Collaboration network diagrams
- Any complex concept that benefits from visualization

For detailed guidance on creating schematics, refer to the scientific-schematics skill documentation.

---

## Workflow for Grant Development

### Phase 1: Planning and Preparation (2-6 months before deadline)

**Activities**:
- Identify appropriate funding opportunities
- Review program announcements and requirements
- Consult with program officers (if appropriate)
- Assemble team and confirm collaborations
- Develop preliminary data (if needed)
- Outline research plan and specific aims
- Review successful proposals (if available)

**Outputs**:
- Selected funding opportunity
- Assembled team with defined roles
- Preliminary outline of specific aims
- Gap analysis of needed preliminary data

### Phase 2: Drafting (2-3 months before deadline)

**Activities**:
- Write specific aims or objectives (start here!)
- Develop project description/research strategy
- Create figures and data visualizations
- Draft timeline and milestones
- Prepare preliminary budget
- Write broader impacts or significance sections
- Request letters of support/collaboration

**Outputs**:
- Complete first draft of narrative sections
- Preliminary budget with justification
- Timeline and management plan
- Requested letters from collaborators

### Phase 3: Internal Review (1-2 months before deadline)

**Activities**:
- Circulate draft to co-investigators
- Seek feedback from colleagues and mentors
- Request institutional review (if required)
- Mock review session (if possible)
- Revise based on feedback
- Refine budget and budget justification

**Outputs**:
- Revised draft incorporating feedback
- Refined budget aligned with revised plan
- Identified weaknesses and mitigation strategies

### Phase 4: Finalization (2-4 weeks before deadline)

**Activities**:
- Final revisions to narrative
- Prepare all required forms and documents
- Finalize budget and budget justification
- Compile biosketches, CVs, and current & pending
- Collect letters of support
- Prepare data management plan (if required)
- Write project summary/abstract
- Proofread all materials

**Outputs**:
- Complete, polished proposal
- All required supplementary documents
- Formatted according to agency requirements

### Phase 5: Submission (1 week before deadline)

**Activities**:
- Institutional review and approval
- Upload to submission portal
- Verify all documents and formatting
- Submit 24-48 hours before deadline
- Confirm successful submission
- Receive confirmation and proposal number

**Outputs**:
- Submitted proposal
- Submission confirmation
- Archived copy of all materials

**Critical Tip**: Never wait until the deadline. Portals crash, files corrupt, and emergencies happen. Aim for 48 hours early.

## Integration with Other Skills

This skill works effectively with:
- **Scientific Writing**: For clear, compelling prose
- **Literature Review**: For comprehensive background sections
- **Peer Review**: For self-assessment before submission
- **Research Lookup**: For finding relevant citations and prior work
- **Data Visualization**: For creating effective figures

---

**Final Note**: Grant writing is both an art and a science. Success requires not only excellent research ideas but also clear communication, strategic positioning, and meticulous attention to detail. Start early, seek feedback, and remember that even the best researchers face rejectionâ€”persistence and revision are key to funding success.

## References

- `references/agency_overview.md`: load first to pick an agency and see its priorities
- `references/core_components.md`: load when drafting any proposal section (summary, aims, approach, data, timeline, team, budget)
- `references/review_criteria_by_agency.md`: load when self-reviewing against NSF, NIH, DOE or DARPA criteria
- `references/writing_principles.md`: load when polishing clarity, argument, figures, risk and coherence
- `references/proposal_types.md`: load when choosing a mechanism or program type
- `references/resubmission_strategies.md`: load when answering reviewer comments (NIH A1, NSF)
- `references/common_mistakes.md`: load for a final pre-submission error sweep
- `references/nsf_guidelines.md`: load for NSF formatting, requirements and strategy
- `references/nih_guidelines.md`: load for NIH mechanisms, review criteria and submission rules
- `references/doe_guidelines.md`: load for DOE programs and application procedures
- `references/darpa_guidelines.md`: load for DARPA BAAs, program offices and strategy
- `references/broader_impacts.md`: load when writing NSF broader impacts
- `references/specific_aims_guide.md`: load when writing a Specific Aims page
- `assets/nsf_project_summary_template.md`: NSF project summary structure; load when drafting that summary
- `assets/nih_specific_aims_template.md`: NIH specific aims page template; load when drafting aims
- `assets/budget_justification_template.md`: budget justification structure; load when writing the budget
