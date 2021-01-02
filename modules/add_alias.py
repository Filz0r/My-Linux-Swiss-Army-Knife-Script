import os

# you can change os.system() for subprocess.run() it should still work


def add_alias():
    print('''
##############################
##
# This script adds armyknife alias to run this script in the end of the
# .bashrc file of the user that ran it
# IT ASSUMES YOU HAVE THE SCRIPT FOLDER IN YOUR HOME DIRECTORY
##
''')
    try:
        username = input(
            'What is the username on your system?: (case sensitive)')
        command = "echo alias armyknife='/home/{}/My-Linux-Swiss-Army-Knife/myLinuxSwissArmyKnife.py' >> /home/{}/.bashrc".format(
            username, username)
        os.system(command)
    except:
        print('There was an error while trying to run this script!')
        return add_alias()

# required part for the script to return to the menu after running its job
    from lib.category_menu import menu
    return menu()
