# [Git](https://git-scm.com/)
Git is a [free and open source](https://git-scm.com/about/free-and-open-source) distributed **version control system** designed to handle everything from small to very large projects with speed and efficiency.

A git repository is just a **Git workspace**. Every repository has it's own history.
- [[gitkraken|GitKraken]] is a GUI for Git.


### Setup
Set the configuration to all the git directories.
```git
git congif --global user.name "usersName"
git congif --global user.mail "usersMail"
```

Set this configuration to this specific directory.
```git
git congif user.name "usersName"
git congif user.mail "usersMail"
```


## [[gitbash|GitBash]]


## [[git workflow|Git Workflow]]

### Commands

- **pwd** - Print Working Directory
- **ls** - List
- **cd** - Change Directory

- git **init**
	 Create an empty Git repository or reinitialize an existing one in the current folder.
- git **status**
	Gives current status of the git repository showing the files added to be used in the next commit.
- git **log**
	Show the commit history.
	**git log --oneline** Show an abbrev of the commits, just the miniHash & name

 
## Commiting

Is a **checkpoint** of the work in that moment. Just save the files that are added to the commit.
- git **add** $fileName$
	Add a/the file(s) to the log. 
		**git add .** -Add all the unstaged files
		**git add -i** Add modified contents 
	
- git **commit**
	Create a commit using the files **added** to the log. It has a name that summarized the changes and work snapshotted in the commit.
		-m Add a message to that commit
```git
	git commit -m "My Message"
	git commiy -a -m "Add all the Unstaged changes"
```

To count the commits for the branch you are on: `git rev-list --count HEAD`

![[GitWorkflow.png]]
- git commit **--amend**
	Used to fix possible errors in the **last commit**.
		Add a forgotten file, change the commit name, etc...


### .gitignore
This is usedful for files you know **never** want to commit.
Including secrets, API keys, credentials, operating system files, log files, dependencies & pckages.
Uses a <.gitignore> file in the root of a repository. Inside we can write patterns to tell Git which files & folers to ignore.
```bash
*.a  # Ignore all .a files
!lib.a  # But do track lib.a, even though you're ignoring .a files above
/TODO  # Only ignore the TODO file in the current directory, not subdir/TODO
build/  # Ignore all files in any directory named build
doc/*.txt  # Ignore doc/notes.txt, but not doc/server/arch.txt
doc/**/*.txt  # Ignore all .txt files in the doc/ directory and any of its subdirectories
```


### Branches
When we built a git repository, the default branch name is **master**. It doesn't do anything special.
![[BranchConcept.png]]
##### HEAD
Is a pointer that refers to the current *location* in your repositoy. Points a particular branch reference. 

#### Create branches
- git **branch**
	List, create or edit branches.
	git **branch** will just list all the branches of the repository.
```git
	git branch -d "branch-name" // Delete that branch
	git branch -m "new-branch-name" // Move/rename branch
```
- git **branch** $branch-name$
	Creates a new branch bases upon the current HEAD. Branch name shouldn't include spaces. Just creates a branch. Doesn't switch to it.
- git **switch** $branch-name$
	Change to another branch.
	Using the **-c** flag to create a new branch & switch to it all in one go.
```git
	git switch -c <branch-name>
```
- git **checkout** $branch-name$
	This **was** the command to switch branches, but it does some additional things, so the decision was made to add a standalone **switch** command which is much simpler.


#### Merge Branches
Makes it supre easy to work within self-contained contexts, but often we want to incorporate changes from one branch to another.

We **merge branches** not specific commits.
We **always merge** the **current HEAD branch**.
![[MergeBranches.png]]
- git **merge** $branch-to-merge-with$
	Merge command will **merge** the **specified branch** with the current **HEAD**.


### Diff
- git **diff**
	aaaa
some text


### Vim Shortcuts
![[vim shortcuts.png]]

----
### Git Documentation
- [git docs](https://git-scm.com/docs)