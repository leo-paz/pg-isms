# Repository instructions

- Treat this repository as a reusable Codex skill library, not an essay-summary collection.
- Follow the `skill-creator` and `writing-skills` skills for every skill package.
- Audit source material before choosing the final skill taxonomy.
- Use subagents for independent essay review and skill forward-testing.
- Do not copy full essays or long passages into this repository. Prefer concise paraphrase, source URL, essay identifier, and exact source lines.
- Keep each `SKILL.md` concise and move detailed evidence into one-level-deep `references/` files.
- Every skill must include valid YAML frontmatter and `agents/openai.yaml`.
- Run a failing baseline evaluation before authoring each behavior-shaping skill, then forward-test the completed skill with fresh context.
- Validate every skill independently before starting the next one.
- Commit and push at meaningful, verified milestones.
