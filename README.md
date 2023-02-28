# Data 210

## Git(hub) refresher

### Setup
#### After creating a new repo on github:

**git clone \<https string>** - clones repo locally and sets origin for you.

#### Locally:

**git init** - creates a new local repo in current directory

### Making changes
**git add** - adds untracked files, use --all flag for convenience

**git commit** - commits tracked changes, use -m \<message> for convenience

**git push** - pushes the local (commited) changes to a remote repo, use 'git push -u origin master' as best practice (sets upstream to the specified branch)

**git pull** - update local repo to the newest version of the remote 

**git status** - prints the current state of the repo, what changes are staged, if up to date with remote repo

### Working with branches
**git branch** - prints existing branches

**git branch \<name>** - creates a new branch with name

**OR**

**git checkout -b \<name>** - creates a new branch with name and swap to it

**git branch -d \<name>** - deletes branch with name

**git diff** - difference between working files and commits

**git log** - log of everything that's happened
## Other version control options
- Gitlab
- Mercurial
- Bitbucket
- Beanstalk
- Perforce
- Apache Subversion
- Azure DevOps Server
- AWS CodeCommit
- Microsoft Team Foundation Server
