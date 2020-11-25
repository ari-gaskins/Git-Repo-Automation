import os
import sys
from dotenv import load_dotenv

# user inputted new directory name
directory = input()

# makes new path
new_path = os.path.join(load_dotenv.PATH, directory)

try:
    os.mkdir(new_path)
except OSError as error:
    print(error)
# those ^ are the first three steps rough draft



