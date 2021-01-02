import os

# you can change os.system() for subprocess.run() it should still work

def sshd_config():
    print('''
##############################
##  
##    -> THIS SCRIPT REQUIRES SUDO
##
##  Opening sshd_config file
##
##############################''')
    os.system('sudo nano /etc/ssh/sshd_config')
    print('''
##############################
##
##  restarting sshd service to apply changes
##
##############################''')
    os.system('sudo systemctl restart sshd')
    # required part for the script to return to the menu after running its job
    from lib.category_menu import menu
    return menu()