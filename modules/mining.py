import os

# you can change os.system() for subprocess.run() it should still work

def mining():
    print('''
##############################
##  
##    -> THIS SCRIPT REQUIRES NANOMINER INSTALLED ON THE SYSTEM
##
##    starting nanominer...
##    make sure your config.ini is in the root folder of the application
##    if you want monitoring windows open them before starting this script
##
##############################''')
#   You have to use the ABSOLUTE PATH for your nanominer file
#   DO NOT FORGET TO add a nanominer config file to the root folder of this program
    os.system('/home/filipe/Documents/nanominer-linux-3.1.2/nanominer')
    # required part for the script to return to the menu after running its job
    from lib.category_menu import menu
    return menu()