import os

# you can change os.system() for subprocess.run() it should still work


def add_alias():
    print('''
##############################
##  
##  This script adds armyknife alias to run this script in the end of the
##  .bashrc file of the user that ran it
##  IT ASSUMES YOU HAVE THE SCRIPT FOLDER IN YOUR HOME DIRECTORY
##
##############################''')
    try:
        username = input('What is the username on your system?: (case sensitive)')
        print(username)
        command = "echo alias armyknife='/home/%d/My-Linux-Swiss-Army-Knife/myLinuxSwissArmyKnife.py' >> /home/%d/.bashrc" % username
        print(command)
        os.system(command)
    except:
        print('you dumb fucker')
        print(username)
        print(command)
        return add_alias()
    
    # required part for the script to return to the menu after running its job
    from lib.category_menu import menu
    return menu()
