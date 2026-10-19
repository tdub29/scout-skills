---
name: cursor-rules
description: "Author .cursor/rules: types, globs, frontmatter"
---

# Cursor Rules

Create and manage Cursor Rules according to the [official Cursor documentation](https://cursor.com/docs/context/rules).

## Quick Start

Run the command:

```bash
npm run generate-cursor-rule
```

Or directly:

```bash
node generate-cursor-rules.js
```

## What the Generator Does

1. Prompt you for a rule name (kebab-case)
2. Ask for a description
3. Let you choose the rule type:
   - **Always Apply**: Applied to every chat session
   - **Apply Intelligently**: Applied when Agent decides it's relevant
   - **Apply to Specific Files**: Applied when files match glob patterns
   - **Apply Manually**: Applied when @-mentioned in chat
4. Collect file patterns (if applicable)
5. Collect the rule content (markdown)
6. Create the rule folder structure in `.cursor/rules/`

## Example Usage

```bash
$ npm run generate-cursor-rule

ðŸŽ¯ Generate Cursor Rule

This will create a new Cursor Rule in .cursor/rules/

Rule name (kebab-case, e.g., "frontend-standards"): frontend-standards
Description (what this rule does): Standards for React components and styling

Rule Type:
1. Always Apply - Apply to every chat session
2. Apply Intelligently - When Agent decides it's relevant
3. Apply to Specific Files - When file matches a pattern
4. Apply Manually - When @-mentioned in chat

Select rule type (1-4): 3
File patterns (comma-separated, e.g., "**/*.tsx", "**/components/**"): **/*.tsx, **/components/**

Enter the rule content (markdown).
You can reference files using @filename.ts syntax.
Press Enter twice when finished, or type "DONE" on a new line:

# Frontend Standards

- Use TypeScript for all components
- Prefer functional components
- Use Tailwind for styling

@component-template.tsx

DONE

âœ… Rule created successfully!
ðŸ“ Location: .cursor/rules/frontend-standards/RULE.md
```

## Rule Structure

Each rule is created as:

```
.cursor/rules/
  your-rule-name/
    RULE.md
```

The `RULE.md` file includes:
- Frontmatter metadata (description, globs, alwaysApply)
- Your rule content in markdown

## Rule Types Explained

### Always Apply
Rules that should be included in every chat session. Use for:
- Project-wide coding standards
- Architecture decisions
- Team conventions

### Apply Intelligently
Rules that the Agent decides to apply based on context. Use for:
- Domain-specific knowledge
- Workflow automation
- Context-dependent guidelines

### Apply to Specific Files
Rules that apply when working with matching files. Use for:
- File-type specific standards (e.g., all `.tsx` files)
- Directory-specific rules (e.g., `components/` folder)
- Pattern-based guidelines

### Apply Manually
Rules that you invoke with @mention. Use for:
- Optional workflows
- Specialized templates
- On-demand guidance

## File References

In your rule content, you can reference files using:

```markdown
@filename.ts
@path/to/file.jsx
```

This includes the file content in the rule's context when applied.

## Best Practices

1. **Keep rules focused**: One rule per concern
2. **Be specific**: Provide concrete examples
3. **Stay under 500 lines**: Split large rules into multiple rules
4. **Version control**: Commit rules with your code
5. **Test rules**: Verify they work as expected in chat

## References

- [Cursor Rules Documentation](https://cursor.com/docs/context/rules)
- See `.cursor/rules/README.md` for more information
- Check `.cursor/rules/example-rule/` for a template
