---
name: git-github-bootstrap
description: Initialize a local project as a Git repository and bind it to a GitHub remote. Use when the user wants to run git init, create a minimal .gitignore, set the default branch, add or update origin, prepare the first commit, connect Git to existing GitHub CLI credentials, or bootstrap a repo before the first push. Triggers include “初始化git”, “初始化 git 仓库”, “初始化仓库”, “Init git”, “init git repo”, “bootstrap repo”, “绑定github仓库”, “绑定 origin”, “bind github repo”, “git init”, “add origin”, “set remote”, and “初始化仓库并推送”.
---

# Git GitHub Bootstrap

Use this skill when the main need is:

- initialize a local folder as a Git repo
- bind a GitHub repository URL
- set or correct `origin`
- prepare the first commit
- connect Git to existing `gh` credentials before first push

This skill is for repository bootstrap.

It is not the main skill for repeated push failure diagnosis. If push starts failing after bootstrap, switch to the existing `github-push` path.

## What This Skill Owns

This skill handles:

1. repository state check
2. `git init` and default branch setup
3. minimal `.gitignore` bootstrap
4. GitHub remote binding
5. first-commit readiness
6. Git credential hookup through `gh auth setup-git`

## Default Bootstrap Flow

Run these checks first:

```bash
pwd
git rev-parse --show-toplevel
git status --short
git branch --show-current
git remote -v
```

Interpretation:

- if `git rev-parse` fails, the folder is not yet a Git repo
- if there is no current branch, initialize with `main`
- if there is no `origin`, add one
- if `origin` exists and already matches the target URL, keep it

## Initialization Rule

If the folder is not a Git repository, initialize it with:

```bash
git init -b main
```

Do not create extra branches during bootstrap unless the user explicitly asks for them.

## .gitignore Rule

Bootstrap should create only the minimum ignore rules needed for the workspace.

Default principle:

- ignore obvious local junk such as `.DS_Store`
- do not blindly exclude project content
- do not remove existing `.gitignore` rules unless the user explicitly asks

If the workspace already has a `.gitignore`, extend it carefully instead of replacing it.

## Remote Binding Rule

Preferred default:

- use `origin` as the GitHub remote name

Decision rule:

- if `origin` does not exist, add it
- if `origin` exists and matches the requested URL, do nothing
- if `origin` exists and differs, only change it when the user clearly asked to bind this project to a different GitHub repo

Commands:

```bash
git remote add origin <url>
git remote set-url origin <url>
```

## Credential Hook Rule

Before the first HTTPS push, check whether `gh` is already authenticated:

```bash
gh auth status
```

If `gh` is already logged in, prefer:

```bash
gh auth setup-git
```

This usually avoids the classic:

```text
fatal: could not read Username for 'https://github.com': Device not configured
```

## First Commit Rule

If the workspace has uncommitted files and the user wants a bootstrap push:

1. stage the intended files
2. create one clear baseline commit
3. only then push

Good baseline commit examples:

- `chore: initialize repository`
- `chore: bootstrap project workspace`
- `chore: initialize proposal workspace`

Do not create vague messages like `first commit` unless the user explicitly prefers that style.

## Push Rule

If the user explicitly asks to push:

1. confirm local branch state
2. confirm `origin`
3. wire Git credentials if possible
4. push `main` to `origin`

Preferred pattern:

```bash
git push -u origin main
```

If HTTPS fails after credential hookup or transport fails repeatedly, stop blind retries and switch to the existing push-diagnosis path.

## Output Format

Use this structure by default:

```markdown
**Bootstrap State**
- Repo:
- Branch:
- Remote:

**Actions**
- ...

**Blockers**
- ...

**Next Step**
- ...
```

## Guardrails

- Do not overwrite a different existing `origin` unless the user asked to rebind the repo.
- Do not invent broad `.gitignore` rules that hide real project content.
- Do not push before a baseline commit exists.
- Do not confuse “GitHub URL reachable” with “Git credentials ready”.
- Do not keep retrying identical pushes after the same auth or transport failure repeats.
