# Notes

# Git Best Practices

## Key Concepts

- Commit hygine and best practices
- Pre-commit and automation
- Common mistakes in real world
- Git at scale
- Git security and secrets hygine

## Commands

`command` - what it does

## Examples

(code examples)

## What I Learned



## Your Notes

To have good commit hygine you should have good commit messages (specific to what the code change does), use squash before merging, one logical change per commit, and avoid noisy merges.

Before committing or pushing code you should do the following pre-commit and automation tasks. You should first run linters/tests before commiting, this is to prevent broken code from entering the repo. You should also add this to you CI pipeline for formatting testing and planning. 

Common real world mistakes made when working with git:
- forgetting to pull before pushing
- force pushing to shared branches (unless necessary)
- committing secrets
- merging without review
- not using .gitignore properly/not commiting secrets or sensitive files

How to manage git repos at scale:
- monorepo strategies (having all services in one repo)
- sparse checkout
- large file support
- clean up legacy history
- Submodules vs subtrees in microservice repos
- Selective CI builds
- Commit linting + bots to enforce rules
- GitOps-style deployments
- Server-side Git hooks

You should never commit secrets and to prevent this from happening use git secrets and .gitignore. If you do commit secrets then you need to fix it fast and clean your history. You should also renew your secrets as soon as possible when this happens. 

