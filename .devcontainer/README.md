# devcontainer

how to use devcontainer with vscode https://code.visualstudio.com/docs/devcontainers/containers

## Quick Start

1. Docker started
2. VS Code and Dev Containers extension installed
2. Open repo in dev container in VS Code
    - Ctrl + Shift + P on windows or CMD + Shift + P on Mac
    - Input Dev Containers, Choose open folder in container


## Resolving Git line ending issues in WSL (resulting in many modified files)：

https://code.visualstudio.com/docs/remote/troubleshooting#_resolving-git-line-ending-issues-in-wsl-resulting-in-many-modified-files

create a file called `.gitattributes` in your project root folder with content as below:

```
* text=auto eol=lf
*.{cmd,[cC][mM][dD]} text eol=crlf
*.{bat,[bB][aA][tT]} text eol=crlf
```

## Sharing Git credentials with your container：

if you are using password/PAT on your local laptop and it is working fine without dev container, then nothing need to be done, but if you are using SSH keys, please follow the guide below:

https://code.visualstudio.com/docs/devcontainers/containers#_sharing-git-credentials-with-your-container



## pre-commit hooks

pre-commit were installed by default in this dev container, if you want to use pre-commit hooks, please create a config file
`.pre-commit-config.yaml`

and execute `pre-commit install`



## How to use pre-commit hooks

### Automatically

if you updated some files/folder which are in the scope of pre-commit checks, for example, *.tf, *.yaml files, the pre-commit hooks will be triggered automatically when you do `git commit`


### Manually

you can manully run the pre-commit command like:

```
pre-commit run --all-files
```

```
pre-commit run <hook_id> --all-files
```

### How to ignore pre-commit hooks

if you want to ignore the pre-commit hooks, please use `--no-verify` in your git commit command, for example

```
git commit -m "update xxxxxxxx" --no-verify
```
