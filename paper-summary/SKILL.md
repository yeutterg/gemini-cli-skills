---
name: paper-summary
description: Extracts and summarizes research papers into an Obsidian note. Creates a file in the Research/ directory with metadata, backlinked authors, key takeaways, and an extremely exhaustive outline.
---

# Research Paper Summary Skill

This skill fetches metadata and text from research papers (ArXiv, PDFs, or local files) and creates a structured summary in your Obsidian Research/ directory.

## Workflow

1. **Identify the Source**: Extract the ArXiv URL, DOI, or local file path from the request.
2. **Fetch Data**: 
   - For ArXiv: Use the bundled Python script to get metadata and abstract.
   - For Local PDFs: Use the `read_file` tool to extract text.
3. **Generate EXHAUSTIVE Outline FIRST**:
   - Trace the paper's structure (Abstract, Intro, Methods, Results, Discussion).
   - Capture every technical specification, formula, dataset, researcher mentioned, and specific result.
   - Go 5-6 levels deep with nesting.
4. **Identify Key Takeaways SECOND**:
   - Review the exhaustive outline.
   - Select the 3-5 most impactful or surprising facts or contributions.
   - Place this section at the top, immediately after the front matter.
5. **Format the Summary**:
   - **Filename**: Save to `Research/[Sanitized Paper Title].md`. Use the full paper title in **Title Case**.
   - **H1 Heading**: Include a `# [Title]` heading in **Title Case** immediately after the front matter.
   - **Front Matter**: 
     - `url`: The source link.
     - `authors`: A YAML list of quoted backlinks (e.g., `  - "[[Name]]"`).
     - `year`: Publication year.
     - `contribution`: 1-sentence summary of what this paper adds to the field.

## Style Guidelines
- **No Spacing**: Do NOT put empty lines between headings or points. Continuous block.
- **Capitalization**: Capitalize the first letter of every bullet point.
- **No Bold**: Do NOT use bold (`**`) anywhere.
- **Indentation**: Use TABS for nesting.
- **Technical Depth**: Use 5-6 levels of nesting for the outline.
	- Level 1: Major section (e.g., Methodology).
	- Level 2: Specific approach or framework.
	- Level 3: Parameters, variables, or datasets.
	- Level 4: Granular procedural details.
	- Level 5: Surprising nuances or technical specs.
	- Level 6: Specific results or edge cases.

## Output Format Template
---
url: [Source URL]
authors:
  - "[[Author 1]]"
year: [YYYY]
contribution: [Key contribution]
---
## Key Takeaways
- Most surprising finding/fact
- Impactful revelation
## Outline
### [Section Title]
- Main point
	- Technical detail
		- Granular spec
			- Specific data point
				- Nuance
					- Citation or edge case
