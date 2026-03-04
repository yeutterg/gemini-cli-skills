---
name: youtube-summary
description: Extracts and summarizes YouTube video transcripts into an Obsidian note. Creates a file in the Research/ directory named after the video with front matter, key takeaways, and an extremely exhaustive, deeply nested outline.
---

# YouTube Summary Skill

This skill fetches transcripts from YouTube videos and creates a structured summary file directly in your Obsidian Vault's Research/ directory.

## Workflow

1. **Identify the YouTube URL**: Extract the URL or Video ID from the user's request.
2. **Fetch Data**: Run the Python script to get the title, URL, and timestamped segments.
   ```bash
   python3 scripts/get_youtube_transcript.py "URL_OR_VIDEO_ID"
   ```
3. **Verify Name Spellings**: 
   - **CRITICAL**: Transcripts often misspell names. 
   - Always prioritize the spelling found in the **Video Title** or official metadata over the transcript text.
   - Example: If the transcript says "Glenn Jeffrey" but the title says "Glen Jeffery", use **Glen Jeffery**.
4. **Generate EXHAUSTIVE Outline FIRST**:
   - Trace the conversation chronologically with maximum possible granularity.
   - Effectively substitute for a full transcript.
   - Capture every technical specification, measurement, researcher name, company, and data point.
   - Go 5-6 levels deep with nesting.
5. **Identify Key Takeaways SECOND**:
   - Review the exhaustive outline.
   - Select only the 3-5 most impactful or surprising facts.
6. **Format the Summary**:
   - **Filename**: Save to `Research/[Sanitized Video Title].md`. **IMPORTANT**: Decode any HTML entities in the title (e.g., convert `&amp;` to `&`).
   - **No H1 Heading**: Do NOT include a `# [Video Title]` heading.
   - **Front Matter**: 
     - `url`: The YouTube URL.
     - `speakers`: A YAML list of quoted backlinks (e.g., `  - "[[Name]]"`). Use verified spellings.
   - **Order**: Key Takeaways immediately follow the front matter, then the Outline, and finally the complete Transcript.
7. **Complete Transcript**:
   - At the very end of the note, add a `## Transcript` section.
   - Use a callout or fold if possible to keep it organized (e.g., `> [!abstract]- Transcript`).
   - Paste the **entire** formatted transcript text provided by the script.
   - **Speaker Attribution**: The script provides `>>` markers where speakers change. Use the context of the video (title, description, and content) to **identify and label the speakers**. Replace `>>` with the speaker's name (e.g., `[05:12] Andrew Huberman: ...`). If unsure, keep the `>>` or use `[05:12] Speaker: ...`.
   - **Timestamps**: Ensure the `[MM:SS]` or `[HH:MM:SS]` timestamps from the script are preserved at the start of paragraphs.

## Style Guidelines
- **No Spacing**: Do NOT put empty lines between headings, subheadings, or bullet points in the Outline or Key Takeaways. Continuous block of text.
- **Transcript Format**: The Transcript section should have paragraphs separated by speaker changes and timestamps for readability.
- **Capitalization**: Capitalize the first letter of every bullet point.
- **No Bold**: Do NOT use bold (`**`) anywhere (except for callout syntax or speaker labels in the transcript).
- **Indentation**: Use TABS for nesting in the outline.
- **Technical Depth**: Use 5-6 levels of nesting for the outline.
- **Timestamp Format**: 
	- Every bullet point in the **Outline** and **Key Takeaways** must end with a timestamp link: `[TIMESTAMP](URL&t=SECONDS)`.
	- In the **Transcript** section, use the bracketed format: `[TIMESTAMP] Speaker Name: Text`.
	- HH:MM:SS format for videos >1hr; MM:SS for <1hr.
	- No outer parentheses or internal spaces around the link in the Outline.

## Output Format Template
---
url: [YouTube URL]
speakers:
  - "[[Speaker 1]]"
---
## Key Takeaways
- Most surprising fact [MM:SS](URL&t=SECONDS)
- Impactful revelation [MM:SS](URL&t=SECONDS)
## Outline
### [Major Section]
- High-level point [MM:SS](URL&t=SECONDS)
	- Specific mechanism [MM:SS](URL&t=SECONDS)
		- Technical data point [MM:SS](URL&t=SECONDS)
			- Granular nuance [MM:SS](URL&t=SECONDS)
				- Specific name/measurement [MM:SS](URL&t=SECONDS)
					- Extra citation/detail [MM:SS](URL&t=SECONDS)
## Transcript
> [!abstract]- Transcript
> [Full raw transcript text here]
