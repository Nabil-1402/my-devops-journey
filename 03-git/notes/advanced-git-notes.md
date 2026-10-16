# Notes

# Advanced Git 

## Key Concepts

- Branching and branch management
- Visualising branches and history
- Rebase vs merge
- Stashing changes
- Reset, revert and cherry-pick
- Forks and pull requests
- Collaboration practices
- Typical Git workflow
- Trunk-based development

## Commands

| Command | Purpose |
| :--- | :--- |
| `git branch` | Lists local branches. |
| `git branch <branch>` | Creates a branch without switching to it. |
| `git checkout -b <branch>` | Creates and switches to a branch using the older syntax. |
| `git switch -c <branch>` | Creates and switches to a branch. |
| `git switch <branch>` | Switches to an existing branch. |
| `git branch -d <branch>` | Deletes a branch, normally only if Git considers it merged. |
| `git merge <branch>` | Merges the named branch into the current branch. |
| `git rebase <branch>` | Replays the current branch's commits on top of the named branch. |
| `git log --oneline --graph --all` | Displays a compact commit graph across branches. |
| `git stash` | Temporarily saves staged and unstaged changes to tracked files. |
| `git stash list` | Lists saved stashes. |
| `git stash apply` | Reapplies the latest stash and keeps it saved. |
| `git stash pop` | Reapplies the latest stash and removes it if application succeeds. |
| `git revert <commit>` | Creates a new commit that reverses another commit's changes. |
| `git reset <commit>` | Moves the current branch to a commit; effects on files depend on the mode. |
| `git cherry-pick <commit>` | Applies a commit's changes to the current branch as a new commit. |

> `git stash` does not include untracked files by default. Use `git stash -u` to include them.

## Examples

```bash
# Create and switch to a feature branch
git switch -c new-branch

# List local branches
git branch

# Merge main into the current feature branch
git merge main

# View history across branches
git log --oneline --graph --all

# Switch back to main
git switch main
```

## What I Learned

I learned how branches isolate work and how to manage them when developing features or collaborating.

I also explored merge, rebase, revert, reset and cherry-pick, including the risks of rewriting shared history. Finally, I learned how stashing supports interruptions and how trunk-based development helps teams integrate changes frequently.

## Your Notes

### Branching

**Branches** let you develop features, test ideas and fix problems separately from the main development branch.

When the work is ready, it can be reviewed and merged into the main branch.

### Merging Branches

**Merging** combines another branch's changes with the current branch.

| Merge Type | What Happens |
| :--- | :--- |
| **Fast-forward** | If the current branch has no separate commits, Git can move its pointer forward to the other branch's commit. |
| **Three-way merge** | If both branches have diverged, Git combines their changes and normally creates a merge commit joining their histories. |

A **merge conflict** occurs when Git cannot automatically combine changes, such as overlapping edits to the same lines.

Conflicts must be resolved before completing the merge.

### Visualising History

```bash
git log --oneline --graph --all
```

This displays a compact graph of commits across branches, making it easier to inspect branching and merging.

### Merge vs Rebase

| Feature | Merge | Rebase |
| :--- | :--- | :--- |
| **Approach** | Joins branch histories. | Replays commits on a new base. |
| **History** | Preserves existing commits. | Creates replacement commits with new hashes. |
| **Result** | May include a merge commit. | Produces a linear sequence of replayed commits. |
| **Typical use** | Integrating work while preserving branch history. | Updating or tidying a feature branch before review. |

Rebasing can make a feature branch's history easier to follow, but rewriting commits that others are using requires coordination.

> Avoid rebasing shared branches unless the team has explicitly agreed on the workflow.

### Stashing Changes

**Stashing** temporarily saves unfinished changes when you need to pause your work, such as to fix an urgent problem on another branch.

| Command | Action |
| :--- | :--- |
| `git stash` | Saves changes to tracked files and returns them to their committed state. |
| `git stash list` | Shows saved stashes. |
| `git stash apply` | Restores changes while keeping the stash. |
| `git stash pop` | Restores changes and removes the stash if successful. |

> Applying a stash can produce conflicts. If `pop` encounters conflicts, Git keeps the stash.

### Revert, Reset and Cherry-Pick

#### Git Revert

`git revert <commit>` creates a **new commit** that reverses the changes introduced by another commit.

It preserves existing history, making it suitable for undoing changes on shared branches.

#### Git Reset

`git reset <commit>` moves the current branch to the selected commit. The mode determines what happens to the staging area and working files.

| Mode | Branch Pointer | Staging Area | Working Files |
| :--- | :--- | :--- | :--- |
| **`--soft`** | Moves to the selected commit. | Unchanged. | Unchanged. |
| **`--mixed`** | Moves to the selected commit. | Resets to that commit. | Unchanged. |
| **`--hard`** | Moves to the selected commit. | Resets to that commit. | Resets tracked files to that commit. |

**Mixed** is the default mode.

> `git reset --hard` discards uncommitted changes to tracked files. It can also remove untracked files or directories that obstruct writing tracked files.

#### Git Cherry-Pick

`git cherry-pick <commit>` applies a selected commit's changes to the current branch as a new commit.

This is useful for **hotfixes or targeted changes** without merging an entire branch.

### Forks and Pull Requests

A **fork** is your own repository copy on a hosting platform such as GitHub.

A typical contribution process is:

1. Fork the original repository.
2. Clone your fork to your local machine.
3. Make changes on a branch.
4. Push the branch to your fork.
5. Open a **Pull Request (PR)** against the original repository.
6. Maintainers review, discuss and potentially merge the changes.

### Collaboration Practices

- Use branches to isolate work.
- Push changes and open pull requests.
- Request reviewers and respond to feedback.
- Resolve conflicts before merging.
- Use Issues, Projects and Discussions to track work.
- Keep commits focused and write clear commit messages.

### Typical Git Workflow

1. Update your local `main` from the remote.
2. Create a feature branch.
3. Make changes, stage them and commit.
4. Push the feature branch.
5. Open a pull request for review.
6. Address feedback and merge the approved changes.
7. Keep local branches synchronised with the remote.

Use merge or rebase to integrate updates according to the team's workflow.

### Trunk-Based Development

**Trunk-based development** involves integrating work into a shared main branch frequently, either directly or through very short-lived branches.

Teams typically support this with:

- Strong CI pipelines
- Reliable automated tests
- Code quality checks
- Small, frequent changes

This approach supports fast delivery, but depends on keeping the main branch healthy.