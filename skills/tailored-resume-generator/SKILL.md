---
name: tailored-resume-generator
description: "Full resume for a pasted job ad. Prefer resume-tailor"
---

# Tailored Resume Generator

## When to Use This Skill

- Applying for a specific job position
- Customizing your resume for different industries or roles
- Highlighting relevant experience for career transitions
- Optimizing your resume for ATS (Applicant Tracking Systems)
- Creating multiple resume versions for different job applications
- Emphasizing specific skills mentioned in job postings

## What This Skill Does

1. **Analyzes Job Descriptions**: Extracts key requirements, skills, qualifications, and keywords from job postings
2. **Identifies Priorities**: Determines what employers value most based on the job description language and structure
3. **Tailors Content**: Reorganizes and emphasizes relevant experience, skills, and achievements
4. **Optimizes Keywords**: Incorporates ATS-friendly keywords naturally throughout the resume
5. **Formats Professionally**: Creates clean, professional resume layouts suitable for various formats
6. **Provides Recommendations**: Suggests improvements and highlights gaps to address

## How to Use

The user supplies a job description plus background details or an existing resume. Input templates, a full worked example and tips for best results are in `references/usage-and-example.md`.

## Instructions

When a user requests resume tailoring:

### 1. Gather Information

**Job Description Analysis**:
- Request the full job description if not provided
- Ask for the company name and job title

**Candidate Background**:
- If user provides existing resume, use it as the foundation
- If not, request:
  - Work history (job titles, companies, dates, responsibilities)
  - Education background
  - Key skills and technical proficiencies
  - Notable achievements and metrics
  - Certifications or awards
  - Any other relevant information

### 2. Analyze Job Requirements

Extract and prioritize:
- **Must-have qualifications**: Years of experience, required skills, education
- **Key skills**: Technical tools, methodologies, competencies
- **Soft skills**: Communication, leadership, teamwork
- **Industry knowledge**: Domain-specific experience
- **Keywords**: Repeated terms, phrases, and buzzwords for ATS optimization
- **Company values**: Cultural fit indicators from job description

Create a mental map of:
- Priority 1: Critical requirements (deal-breakers)
- Priority 2: Important qualifications (strongly desired)
- Priority 3: Nice-to-have skills (bonus points)

### 3. Map Candidate Experience to Requirements

For each job requirement:
- Identify matching experience from candidate's background
- Find transferable skills if no direct match
- Note gaps that need to be addressed or de-emphasized
- Identify unique strengths to highlight

### 4. Structure the Tailored Resume

**Professional Summary** (3-4 lines):
- Lead with years of experience in the target role/field
- Include top 3-4 required skills from job description
- Mention industry experience if relevant
- Highlight unique value proposition

**Technical/Core Skills Section**:
- Group skills by category matching job requirements
- List required tools and technologies first
- Use exact terminology from job description
- Only include skills you can substantiate with experience

**Professional Experience**:
- For each role, emphasize responsibilities and achievements aligned with job requirements
- Use action verbs: Led, Developed, Implemented, Optimized, Managed, Created, Analyzed
- **Quantify achievements**: Include numbers, percentages, timeframes, scale
- Reorder bullet points to prioritize most relevant experience
- Use keywords naturally from job description
- Format: **[Action Verb] + [What] + [How/Why] + [Result/Impact]**

**Education**:
- List degrees, certifications relevant to position
- Include relevant coursework if early career
- Add certifications that match job requirements

**Optional Sections** (if applicable):
- Certifications & Licenses
- Publications or Speaking Engagements
- Awards & Recognition
- Volunteer Work (if relevant to role)
- Projects (especially for technical roles)

### 5. Optimize for ATS (Applicant Tracking Systems)

- Use standard section headings (Professional Experience, Education, Skills)
- Incorporate exact keywords from job description naturally
- Avoid tables, graphics, headers/footers, or complex formatting
- Use standard fonts and bullet points
- Include both acronyms and full terms (e.g., "SQL (Structured Query Language)")
- Match job title terminology where truthful

### 6. Format and Present

**Format Options**:
- **Markdown**: Clean, readable, easy to copy
- **Plain Text**: ATS-optimized, safe for all systems
- **Tips for Word/PDF**: Provide formatting guidance

**Resume Structure Guidelines**:
- Keep to 1 page for <10 years experience, 2 pages for 10+ years
- Use consistent formatting and spacing
- Ensure contact information is prominent
- Use reverse chronological order (most recent first)
- Maintain clean, scannable layout with white space

### 7. Provide Strategic Recommendations

After presenting the tailored resume, offer:

**Strengths Analysis**:
- What makes this candidate competitive
- Unique qualifications to emphasize in cover letter or interview

**Gap Analysis**:
- Requirements not fully met
- Suggestions for addressing gaps (courses, projects, reframing experience)

**Interview Preparation Tips**:
- Key talking points aligned with resume
- Stories to prepare based on job requirements
- Questions to ask that demonstrate fit

**Cover Letter Hooks**:
- Suggest 2-3 opening lines for cover letter
- Key achievements to expand upon

### 8. Iterate and Refine

Ask if user wants to:
- Adjust emphasis or tone
- Add or remove sections
- Generate alternative versions for different roles
- Create format variations (traditional vs. modern)
- Develop role-specific versions (if applying to multiple similar positions)

### 9. Best Practices to Follow

**Do**:
- Be truthful and accurate - never fabricate experience
- Use industry-standard terminology
- Quantify achievements with specific metrics
- Tailor each resume to specific job
- Proofread for grammar and consistency
- Keep language concise and impactful

**Don't**:
- Include personal information (age, marital status, photo unless requested)
- Use first-person pronouns (I, me, my)
- Include references ("available upon request" is outdated)
- List every job if career is 20+ years (focus on relevant, recent experience)
- Use generic templates without customization
- Exceed 2 pages unless very senior role

### 10. Special Considerations

Variants for career changers, recent graduates, senior executives, technical roles and creative roles are in `references/special-considerations.md`.

---

## Privacy Note

This skill processes your personal and professional information to generate tailored resumes. Always review the output before submitting to ensure accuracy and appropriateness. Remove or modify any information you prefer not to share with potential employers.

## References

- `references/usage-and-example.md`: load when asking the user for input, showing what a good request looks like, or matching the output shape of the worked example
- `references/special-considerations.md`: load when the candidate is a career changer, recent graduate, senior executive, or in a technical or creative role
