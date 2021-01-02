import os

# you can change os.system() for subprocess.run() it should still work

def ufw_basic():
    print('''
##############################
##  
##    -> THIS SCRIPT REQUIRES SUDO
##
##  This script installs UFW on the server
##  Creates a couple of default rules an then activates the firewall
##
##############################''')
    os.system('sudo apt install ufw -y')
    os.system('sudo ufw default deny incoming')
    os.system('sudo ufw default allow outgoing')
    os.system('sudo ufw allow ssh')
    os.system('sudo ufw enable')
    print('''
##############################
##  
##  UFW is now set up and installed, keep in mind that
##  YOU CAN ONLY RUN THIS SCRIPT ON SERVERS
##  Running it on a desktop will result in a loss of
##  internet connectivity!!
##
##############################''')
    # required part for the script to return to the menu after running its job
    from lib.category_menu import menu
    return menu()