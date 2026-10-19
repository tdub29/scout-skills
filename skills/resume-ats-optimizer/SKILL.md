---
name: resume-ats-optimizer
description: "Match one resume to one posting's ATS keywords"
---

# Resume ATS Optimizer

## When to Use This Skill

Use this skill when the user wants to:
- Optimize their resume for Applicant Tracking Systems (ATS)
- Check if their resume will pass automated screening
- Understand why their applications aren't getting responses
- Mentions keywords like: "ATS", "not getting interviews", "resume not working", "optimize resume", "keyword optimization"

Also use when the user provides a resume file and mentions they're applying to jobs.

## Core Capabilities

- Parse resume and test ATS compatibility
- Extract and analyze keywords against job descriptions
- Identify formatting issues that break ATS parsers
- Calculate match scores between resume and job postings
- Suggest keyword additions and placements
- Generate ATS-friendly formatting recommendations

## The ATS Problem

75% of resumes are rejected by Applicant Tracking Systems before a human ever sees them. Companies use ATS to:
- Filter out unqualified candidates automatically
- Search for specific keywords from job requirements
- Parse resumes into structured data
- Rank candidates by keyword match percentage

Common reasons resumes fail ATS:
1. Poor formatting (tables, columns, headers/footers)
2. Missing keywords from job description
3. Inconsistent section headers
4. Non-standard fonts or special characters
5. Text embedded in images
6. Incorrect file format

## ATS Compatibility Checklist

### File Format
- âœ… Use .docx or .pdf (not .pages, .odt)
- âœ… PDF must be text-based, not scanned image
- âœ… File name: "FirstName_LastName_Resume.pdf"

### Font & Formatting
- âœ… Standard fonts: Arial, Calibri, Georgia, Times New Roman
- âœ… Font size: 10-12pt for body, 14-16pt for headers
- âœ… No text boxes, tables, or columns
- âœ… No headers/footers (put contact info in body)
- âœ… No images, graphics, or charts
- âœ… Consistent date formats (MM/YYYY)
- âœ… Standard bullet points (â€¢, -, *)

### Section Headers
Use standard, recognizable headers:
- âœ… "Professional Experience" or "Work Experience" (not "Where I've Been")
- âœ… "Education" (not "Academic Background")
- âœ… "Skills" (not "Core Competencies")
- âœ… "Summary" or "Professional Summary"

### Contact Information
```
John Smith
email@example.com | (555) 123-4567 | LinkedIn: linkedin.com/in/johnsmith
San Francisco, CA
```

NOT in header/footer, and avoid:
- âŒ Tables for contact info
- âŒ Special characters in email
- âŒ Multiple phone numbers
- âŒ Full mailing address (city/state is enough)

## Keyword Optimization Process

### Step 1: Extract Job Description Keywords

Identify three types of keywords:

**Hard Skills (Technical)**
- Programming languages (Python, Java, SQL)
- Tools and platforms (Salesforce, AWS, Excel)
- Certifications (PMP, CPA, CFA)
- Methodologies (Agile, Six Sigma, SDLC)

**Soft Skills**
- Leadership, collaboration, communication
- Problem-solving, analytical thinking
- Project management, stakeholder management

**Industry Terms**
- B2B, SaaS, e-commerce
- Enterprise, SMB, mid-market
- ARR, MRR, churn rate

### Step 2: Match Analysis

For each keyword in job description:
1. Check if exact phrase appears in resume
2. Check for synonyms or variations
3. Count frequency of mention
4. Note location (summary, experience, skills)

### Step 3: Calculate Match Score

```
Match Score = (Keywords Matched / Total Required Keywords) Ã— 100

Example:
Job has 20 required keywords
Your resume has 15 of them
Match Score = 75%

Target: 80%+ for strong match
```

### Step 4: Keyword Placement Strategy

Load `references/keyword-placement.md` when deciding where each keyword goes in the resume.

## Analysis Output Format

Load `references/analysis-output-format.md` before writing the final analysis; follow its structure.

## Common ATS Failure Patterns

Load `references/failure-patterns.md` when diagnosing creative formatting, odd section names, missing keywords, or keyword stuffing.

## Industry-Specific Considerations and Edge Cases

Load `references/industry-and-edge-cases.md` for tech, finance, healthcare, marketing, career changers, graduates, executives, or employment gaps.

## Implementation Checklist

When helping user optimize for ATS:

1. âœ… Scan current resume for ATS compatibility issues
2. âœ… Analyze job description for required keywords
3. âœ… Calculate current match score
4. âœ… Identify specific missing keywords
5. âœ… Suggest exact placements for new keywords
6. âœ… Flag formatting problems
7. âœ… Provide before/after examples
8. âœ… Re-score after suggested changes
9. âœ… Verify file format and naming
10. âœ… Test with ATS simulator if possible

## Success Metrics

After optimization, the resume should:
- Score 80%+ match for target job descriptions
- Pass ATS parsing test (all sections recognized)
- Have zero formatting errors
- Include all critical keywords 2-4x each
- Read naturally (not keyword-stuffed)
- Be ready to submit immediately

## References

- `references/keyword-placement.md`: load at Step 4 when placing keywords
- `references/analysis-output-format.md`: load before writing the final analysis report
- `references/failure-patterns.md`: load when diagnosing why a resume fails ATS parsing or ranking
- `references/industry-and-edge-cases.md`: load for industry guidance and edge cases (career changers, graduates, executives, gaps)
