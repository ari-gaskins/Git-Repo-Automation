import os
import sys
from dotenv import load_dotenv
from github import Github

# load in .env file contents
load_dotenv()

path = os.getenv('PATH')
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

def create():
    # create foldername as first argument
    folderName = str(sys.argv[1])
    os.mkdir(path + str(folderName))
    # github methods
    user = Github(username, password).get_user()
    # create repo with github method
    repo = user.create_repo(folderName)
    # prints folderName to where the brackets are
    # allows you to print variables as string 
    print('Successfully created repo {}'.format(folderName))

# helps module understand whether its being run directly or referenced in another program
if __name__ == '__main__':
    # in this case program is run directly
    create()
# else:
    # program is referenced in another program



