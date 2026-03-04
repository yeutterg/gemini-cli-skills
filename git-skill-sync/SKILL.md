---
name: git-skill-sync
description: Commits and pushes all skills in the /Users/greg/.gemini/skills/ directory to the remote GitHub repository (https://github.com/yeutterg/gemini-cli-skills). Use this to keep the remote skills repository in sync with the local workspace.
---
# Skill Sync

This skill synchronizes the local `.gemini/skills/` directory with the remote GitHub repository.

## Workflow

1. **Verify Git Repository**: Ensure the command is run within the `.gemini/skills/` directory and that it is a valid Git repository with the remote `origin` set to `https://github.com/yeutterg/gemini-cli-skills.git`.
2. **Stage Changes**: Add all new, modified, and deleted files in the directory.
   ```bash
   git add .
   ```
3. **Commit Changes**: Create a commit with a descriptive, timestamped message.
   ```bash
   git commit -m "Sync skills: $(date +'%Y-%m-%d %H:%M:%S')"
   ```
4. **Push to Remote**: Push the changes to the `main` branch of the remote repository.
   ```bash
   git push origin main
   ```

## Guidelines
- **Scope**: Only operate within the `.gemini/skills/` directory.
- **Safety**: Do not push if there are merge conflicts. Report any errors to the user.
- **Verification**: After pushing, confirm the success of the operation.
