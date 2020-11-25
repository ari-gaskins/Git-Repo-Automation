import os
import sys
from dotenv import load_dotenv

# base path
parent_dir = "/home/USER/Documents/Github"

# user inputted new directory name
directory = input()

# makes new path
path = os.path.join(parent_dir, directory)

try:
    os.mkdir(path)
except OSError as error:
    print(error)

