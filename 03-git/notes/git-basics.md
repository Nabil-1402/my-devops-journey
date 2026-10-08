# Notes

# Git Fundementals and basics

## Key Concepts

- Git is a version control tool used to help developers
- Git is a distributed system
- Git is not a file tracker

## Git Terminology and commands

`Repository` - A Git project containing your files and a `.git` directory that stores version history and metadata.

`Commit` - A snapshot of your tracked files, with metadata such as the author, timestamp, message, and parent commit(s).

`Branch` - A movable pointer to a commit, such as `main`, `dev`, or `feature/login`.

`Remote` - A named reference to another repository, often hosted on GitHub or GitLab. The default name is usually `origin`.

`Staging Area` - Also called the index. Holds the changes you have selected to include in your next commit.

`Blob` - Stores the contents of a file, without its filename or path.

`Tree` - Represents a directory snapshot, storing entry names, file modes, and pointers to blobs (files) or other trees (subdirectories).

`Refs (References)` - Names that point to Git objects, including branches under `refs/heads/` and tags under `refs/tags/`.

`HEAD` - Points to your current branch, or directly to a commit when in detached HEAD state.

`Index` - Usually the binary file `.git/index`, which stores staging area information.

`Object Store` - Located in `.git/objects/`. Stores blobs, trees, commits, and annotated tags, identified by their hashes.

`Tag` - A named reference marking a particular point in history, often a release such as `v1.0`.

`git init` - Initialises a Git repository, creating a `.git` directory.

`git add` - Stages changes for the next commit.

`git commit` - Saves the staged changes as a snapshot in the repository's history.

`git status` - Shows staged changes, unstaged changes, and untracked files.

`git log` - Shows the commit history.

`git diff` - Shows unstaged changes. Use `git diff --staged` to see staged changes.

`git config` - Configures Git settings, such as your author name and email address.

`git help <command>` - Opens the built-in documentation for a Git command.

`git clone` - Creates a local copy of an existing repository.

`git rm` - Removes tracked files and stages their deletion.

`git mv` - Moves or renames tracked files and stages the change.

`git restore` - Restores files, discarding unstaged changes by default. Use `git restore --staged` to unstage changes.

## Examples

git add <file_name>

git commit -m "commit message"

git push 

git checkout -b new-branch

## What I Learned

I Learned that Git is a powerful version control tool that helps people manage their work especially in team settings. Git provides visibility and accountability. Having a place to be able to see your history makes reverting changes much easier and same with collaborative work. Unlike old tools like SVN there's no file locking in git. There is a central remote repo and all team members can have their own local repo to work on and push changes from their local to the remote.

## Your Notes

Every git repo has a secret folder called `.git`. This directory is the "brain" of your git project/directory. This holds everything git needs to function: history, configurations, branches, etc. `.git/ref` this is where git stores branches and tags. `.git/objects`, this is also called object store and it is where git keeps every commit, blob and tree. This is all compressed and stored by SHA hash. `.git/config` stores all the repo configuration settings, such as having different remotes or users for a project, it will go here. `.git/HEAD` is a key file and tells git what branch your commit is currently on. `.git/index` is the staging area, that is like a temporary zone between editing your files and committing them.   

Typical git workflow:
 - working directory -> git status -> git add (staging area) -> git commit -> git push (remote repo)


Being able to look at the Git history is crucial especially for a DevOps engineer. The following are useful commands for helping you do that: git log, git log --online --graph (shows a clean visual branch layout), git show <commit> (view a specific commit), git diff, git diff --staged (compare staged to last commit), git blame <file> (show who last changed each line) and git reflog (view local HEAD history). 

Git gives you visibility and accountabilty.



