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

`git stash` - temporarily save uncomitted changes

`git stash list` - view all stashes

`git stash apply` - reapply latest stash (keeps stash)

`git stash pop` - reappply and delete the stash

`git revert` - create a new commit that undoes another. 

`git reset` - move branch pointer backwards

`git cherry-pick` - apply a single commit from another branch


## Examples

git checkout -b new-branch

git switch main

git merge main

git branch

## What I Learned

I learned what branches are, why they are used and how they are used. I also learned about how to manage your git history by using commands like git revert, reset and cherry-pick and also the associated dangers of altering histroy. I also learned the collaborative practices of using git and how some companies use trunk based development to ship out features quickly. Finally I also learned about stashing changes to save current work when you need to urgently fix a problem on another branch.


## Your Notes

Branches let you work on multiple things at once without messing up your main project. This is best for testing a new feature or developing something new for the project. 

When you are done working on a branch and want that code to be moved and implemented on your main project, you merge it. This means combining changes from one branch into another. We can handle merge in two ways, if nothing has happend or nothing has changed in main since the feature branch has been created, Git can perform a fast forward merge. You move the pointer forward. But if both branches have diverged Git does a recursive merge(true merge). This creates a merge commit which ties both histories together. If the same file has been edited on both sides then Git might not know what to do and this is called a **merge conflict**. You have to resolve this manually. 


`git log --oneline --graph --all` is the best command for viewing your commit history and logs. This tells you everything (branches, merges and history) in one clear view. Eespecially useful you are merging branches and you want to actually make sure what actually happend. 

Merge is safe and friendly, it brings two branches together and preserves the full history. It also adds a merge commit so you can always see where the branches joined and this is really good for collaborative work. Rebase rewrites your history. This provides a linear commit timeline and is perfect for when you want to clean up your branch before opening a pull request. You should not rebase shared branches as rewriting history that others are using can break stuff and confuse everyone. 

When you are halfway through making some changes and you need to switch to another branch suddenly and you are not ready to commit that is where you use git stash. This is a temporary storage box for your changes. 

Git revert, reset and cherry-pick all deal with history. Git revert is the more 'safer' one. Here creates a new commit that undoes another. It does not mess with the history which means it is fine to use in shared branches. Git reset is more on the aggressive side. This moves the branch pointer backwards. There are 3 types of git reset: soft, mixed and hard. Soft moves your pointer back but keeps your changes staged. Mixed moves the pointer back but also unstages your changes. Hard nukes everything so you have to use it with care. Git cherry-pick is useful as it lets you take a certain commit from another branch and apply it to your own. This is useful for hot fixes or targeted chanegs. 

• Fork = your own copy of someone else's repo (on GitHub)
• Clone the forked repo to your local machine
• Make changes → push to your fork
• Open a Pull Request (PR) to propose your changes
• Used in open source and cross-team workflows
• Original repo owner can review, comment, and merge


Collaboraing practices:
- Use branches to isolate work
- Push to remote and open Pull Requests
- Assign reviewers, use GitHub's UI for comments
- Resolve conflicts before merge
- Use Issues, Projects, Discussions to track work
- Keep commits focused and

Typical workflow in git is to first pull latest from main, then create a feature branch then stage, commit and push your work onto your branch. When that is done then open a PR (pull request) so that code can be reviewed and merged to main. Then regularly sync your local with the remote using git pull, rebase and merge. 

Trunk based development is when everyone is working directly on the main branch or on very short lived branches that quickly get merged to main. To make this work safely these teams usually have very strong CI pipelines and a lot of code quality checks. This is good for fast paced environments but requires high test coverage. 