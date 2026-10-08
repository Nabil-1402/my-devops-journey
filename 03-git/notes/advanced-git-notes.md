# Notes

# Advanced Git 

## Key Concepts

- Branching and branch management
- Visualise branches and logs
- Rebase vs merge
- Stash and pop
- Reset, revert and cherry pick
- Forks and pull requests
- Collaborating practices
- Typical Git workflow
- Trunk-based development

## Commands

`git branch` - list/create branches

`git checkout -b <branch>` - create and switch to a branch (old syntax)

`git switch -c branch` - create and switch branch (modern syntax)

`git switch branch` - safely switch branch

`git branch -d branch` - delete a branch

`git merge <branch>` - merge target into current branch


## Examples

(code examples)

## What I Learned



## Your Notes

Branches let you work on multiple things at once without messing up your main project. This is best for testing a new feature or developing something new for the project. 

When you are done working on a branch and want that code to be moved and implemented on your main project, you merge it. This means combining changes from one branch into another. We can handle merge in two ways, if nothing has happend or nothing has changed in main since the feature branch has been created, Git can perform a fast forward merge. You move the pointer forward. But if both branches have diverged Git does a recursive merge(true merge). This creates a merge commit which ties both histories together. If the same file has been edited on both sides then Git might not know what to do and this is called a **merge conflict**. You have to resolve this manually. 


`git log --oneline --graph --all` is the best command for viewing your commit history and logs. This tells you everything (branches, merges and history) in one clear view. Eespecially useful you are merging branches and you want to actually make sure what actually happend. 

Merge is safe and friendly, it brings two branches together and preserves the full history. It also adds a merge commit so you can always see where the branches joined and this is really good for collaborative work. Rebase rewrites your history. This provides a linear commit timeline and is perfect for when you want to clean up your branch before opening a pull request. You should not rebase shared branches as rewriting history that others are using can break stuff and confuse everyone. 
