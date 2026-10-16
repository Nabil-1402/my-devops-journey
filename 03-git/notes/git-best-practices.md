# Notes

# Git Best Practices

## Key Concepts

- Commit hygiene and best practices
- Pre-commit checks and automation
- Common real-world mistakes
- Managing Git repositories at scale
- Git security and secrets hygiene

## What I Learned

I learned how good commit hygiene makes changes easier to understand and review, especially in a team.

I also explored how automated checks, such as linters and tests, help catch problems before changes reach shared branches. Finally, I learned how to prevent accidental secret exposure and respond if it happens.

## Your Notes

### Commit Hygiene

Good commit hygiene keeps a repository's history clear and useful.

- **Write specific commit messages:** Explain what changed and why.
- **Keep commits focused:** Include one logical change per commit.
- **Squash when appropriate:** Combine unnecessary intermediate commits before merging, following the team's workflow.
- **Avoid noisy merges:** Keep history understandable without unnecessary merge commits.

### Pre-Commit Checks and Automation

Before committing or pushing:

- Run **linters** to catch code quality issues.
- Run **formatters** to maintain consistent styling.
- Run relevant **tests** to catch broken behaviour.
- Use **pre-commit hooks** to automate local checks.

Include relevant checks in the **CI pipeline** too, such as formatting, testing and infrastructure planning.

> Local hooks provide early feedback, but CI checks are still needed because local hooks can be skipped.

### Common Real-World Mistakes

| Mistake | Better Practice |
| :--- | :--- |
| **Pushing without checking remote updates** | Fetch and integrate changes when needed before pushing. |
| **Force-pushing to shared branches** | Avoid rewriting shared history without team coordination. |
| **Committing secrets** | Use secret scanning and keep credentials out of version control. |
| **Merging without review** | Follow the team's pull request and review process. |
| **Misusing `.gitignore`** | Exclude local configuration, generated files and sensitive files appropriately. |

### Managing Git at Scale

| Approach | Purpose |
| :--- | :--- |
| **Monorepo strategies** | Manage multiple services or projects in one repository. |
| **Sparse checkout** | Limit which tracked files appear in the working directory. |
| **Git LFS** | Manage large files outside Git's normal object storage. |
| **History cleanup** | Remove obsolete or problematic historical content when justified and coordinated. |
| **Submodules and subtrees** | Include or reference other repositories within a project. |
| **Selective CI builds** | Run relevant checks and builds based on what changed. |
| **Commit linting and bots** | Enforce agreed commit conventions and automate routine tasks. |
| **GitOps-style deployments** | Use version-controlled desired configuration to drive deployments. |
| **Server-side Git hooks** | Enforce checks when the hosting platform supports them. |

### Git Security and Secrets Hygiene

Never commit secrets such as **API keys, passwords, tokens or private keys**.

To reduce the risk:

- Use `.gitignore` to exclude sensitive local files.
- Use secret-scanning tools such as `git-secrets`.
- Review staged changes before committing.

> `.gitignore` does not protect files that Git already tracks, and it does not scan file contents for secrets.

### If a Secret Is Committed

1. **Revoke or rotate the secret immediately.**
2. Remove it from the current code and use an appropriate secret-management method.
3. Clean it from repository history where necessary, coordinating any history rewrite with collaborators.
4. Check for exposure in remote repositories, logs and other copies.

> Removing a secret from the latest commit does not remove it from earlier history. Cleaning history does not make an exposed credential safe to reuse.