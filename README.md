# Git-Repo-Automation

A python project idea I got from Kalle Hallden. This project is intended to automate the process of initializing and creating a git repository in the terminal. The goal is to use one command to do so.


## Project Notes

Steps to initialize and create repo
1) cd Documents/GitHub
2) mkdir <folder name> 
3) cd <folder>
4) git init
5) touch README.md
6) git add .
7) git commit -m "initial commit"
8) make repo on github.com
9) copy the repo https
10) git remote add origin <https>
11) git push -u origin master
12) code .

- created .env file and settings.py which will hold internal settings for the program and not be shown
- make code to give command function
- import os for bash commands in python 
- subprocess.run(args, capture_output = TRUE) will let you do the command and then see output
- example: subprocess.Popen("usr/bin/git", "commit", "-m", "Fixed a bug")
- need run vim .bashrc to access commands
- make "create" command using  alias
- ideally alias create='create.py'
- run source ~/.bashrc to refresh file
- test command

## Links

https://thispointer.com/how-to-change-current-working-directory-in-python/
shows how to change directory

https://www.geeksforgeeks.org/custom-commands-linux-terminal/
shows how to name aliases using text editor in .bashrc

https://docs.python.org/3/library/subprocess.html?highlight=subprocess#module-subprocess
subprocess class documentation

https://docs.python.org/3/library/os.html?highlight=os#module-os
os class documentation

https://janakiev.com/blog/python-shell-commands/#:~:text=A%20common%20thing%20to%20do,the%20os%20and%20subprocess%20modules.
a bit of a difficult explanation of subprocess and os uses

https://medium.com/devnetwork/how-to-create-your-own-custom-terminal-commands-c5008782a78e
more on custom files, might come in handy

https://dbader.org/blog/how-to-make-command-line-commands-with-python
^important: shows how to make python script terminal executable

https://www.geeksforgeeks.org/python-os-mkdir-method/
helps see mkdir() operations and os.path.join() usage

https://pypi.org/project/python-dotenv/
how to use python-dotenv