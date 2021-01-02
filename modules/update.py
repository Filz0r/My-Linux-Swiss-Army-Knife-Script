import os

# you can change os.system() for subprocess.run() it should still work

def update():
    print('''
##############################
##  
##    -> THIS SCRIPT REQUIRES SUDO
##
##############################''')
    os.system('sudo apt update')
    os.system('sudo apt upgrade -y')
    # required part for the script to return to the menu after running its job
    from lib.category_menu import menu
    return menu()
