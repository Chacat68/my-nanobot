---
name: skills-sh
description: Search and install agent skills from skills.sh, the open agent skills ecosystem by Vercel.
homepage: https://skills.sh/
metadata: {"nanobot":{"emoji":"🧩","requires":{"bins":["npx"]}}}
---

# skills.sh

Open skill registry and CLI for installing reusable agent capabilities.

## When to use

Use this skill when the user asks any of:
- "install a skill from skills.sh"
- "browse skills.sh"
- "find a skill on skills.sh"
- "add a skill from GitHub"
- "install vercel agent skills"

## Browse

Visit the registry in a browser:

```text
https://skills.sh/
```

## Install

Install a published skills collection directly with the CLI:

```bash
npx skills add <owner/repo>
```

Example:

```bash
npx skills add vercel-labs/agent-skills
```

If the user gives a skills.sh page URL, extract the `<owner/repo>` identifier from it and use that with `npx skills add`.

## Notes

- Requires Node.js and `npx`.
- skills.sh is a public ecosystem; review skills before installing.
- If installation targets a global agent directory outside the current workspace, tell the user where the files were installed.
- After install, remind the user to start a new session so the new skill is loaded.