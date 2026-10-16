# Notes

# Git Fundementals and basics

## Key Concepts

- Git is a version control tool for managing changes and collaboration.
- Git is distributed: each full clone has its own repository history.
- Git records snapshots of tracked content, rather than just a list of file changes.

## Git Terminology

| Term | Meaning |
| :--- | :--- |
| **Repository** | A Git project containing your files and a `.git` directory that stores history and metadata. |
| **Commit** | A snapshot of tracked content, with metadata such as the author, timestamp, message and parent commit(s). |
| **Branch** | A movable pointer to a commit, such as `main`, `dev` or `feature/login`. |
| **Remote** | A named connection to another repository, often hosted on GitHub or GitLab. A common name is `origin`. |
| **Staging Area / Index** | Holds the changes selected for the next commit. |
| **Blob** | Stores file contents without the filename or path. |
| **Tree** | Represents a directory snapshot, storing names, file modes and references to blobs or other trees. |
| **Refs — References** | Names pointing to Git objects, including branches and tags. |
| **HEAD** | Identifies the current branch, or points directly to a commit in detached HEAD state. |
| **Object Store** | Stores Git objects, including blobs, trees, commits and annotated tags, identified by hashes. |
| **Tag** | A named reference marking a point in history, often a release such as `v1.0`. |

## Common Commands

| Command | Purpose |
| :--- | :--- |
| `git init` | Initialises a Git repository. |
| `git clone <url>` | Creates a local copy of an existing repository. |
| `git add <file>` | Stages changes for the next commit. |
| `git commit -m "message"` | Records the staged snapshot in the repository's history. |
| `git status` | Shows staged changes, unstaged changes and untracked files. |
| `git log` | Displays commit history. |
| `git diff` | Shows unstaged changes to tracked files. |
| `git diff --staged` | Compares staged changes with the latest commit. |
| `git config` | Reads or updates Git settings, such as author name and email. |
| `git help <command>` | Opens documentation for a Git command. |
| `git rm <file>` | Removes a tracked file and stages its deletion. |
| `git mv <old> <new>` | Moves or renames a tracked file and stages the change. |
| `git restore <file>` | Restores a file from the index, discarding its unstaged changes. |
| `git restore --staged <file>` | Unstages changes while keeping the working files. |
| `git push` | Sends local commits and updates references in a remote repository. |

## Examples

```bash
# Check the current state
git status

# Stage a file
git add <file_name>

# Commit the staged changes
git commit -m "Describe the change"

# Push commits to the configured upstream
git push

# Create and switch to a new branch
git checkout -b new-branch
```

## What I Learned

I learned how Git helps developers manage changes, collaborate and maintain visibility into a project's history.

Its history makes it easier to investigate changes and revert work when needed. Git supports parallel development without requiring file locking in its normal workflow.

Because Git is distributed, team members can work and commit locally, then share changes through a remote repository. A shared central remote is a common workflow, but Git does not require one.

## Your Notes

### The `.git` Directory

Each standard Git repository has a hidden `.git` directory containing the information Git needs to manage the project.

| Path | Purpose |
| :--- | :--- |
| `.git/refs/` | Stores references such as branches and tags. Some references may also be packed. |
| `.git/objects/` | Stores compressed Git objects, identified by their hashes. |
| `.git/config` | Stores repository-specific settings, including remotes and local configuration. |
| `.git/HEAD` | Identifies the current branch or a directly checked-out commit. |
| `.git/index` | Stores staging area information for the next commit. |

### Typical Git Workflow

1. Edit files in the **working directory**.
2. Run `git status` to inspect changes.
3. Use `git add` to select changes for the **staging area**.
4. Use `git commit` to record the staged snapshot **locally**.
5. Use `git push` to share commits with the **remote repository**.

### Inspecting Git History

Understanding Git history is useful for troubleshooting, reviewing changes and tracing issues in DevOps work.

| Command | Purpose |
| :--- | :--- |
| `git log` | Displays commit history. |
| `git log --oneline --graph` | Shows a compact history with a visual commit graph. |
| `git show <commit>` | Displays a specific commit and its changes. |
| `git diff` | Shows unstaged changes to tracked files. |
| `git diff --staged` | Shows staged changes compared with the latest commit. |
| `git blame <file>` | Shows the commit and author responsible for the last change to each line. |
| `git reflog` | Shows locally recorded reference movements, including recent HEAD changes. |

Git provides **visibility, traceability and accountability** throughout a project's development.