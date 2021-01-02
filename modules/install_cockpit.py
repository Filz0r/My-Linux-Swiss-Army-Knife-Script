import os

# you can change os.system() for subprocess.run() it should still work

def install_cockpit():
    print('''
##############################
##  
##    -> THIS SCRIPT REQUIRES SUDO
##
##  This script installs cockpit on the server
##  Enables and starts it
##  And adds port 9090 as an exception to UFW
##
##############################''')
    os.system('sudo apt install cockpit -y')
    os.system('sudo systemctl enable cockpit')
    os.system('sudo systemctl start cockpit')
    os.system('sudo ufw allow 9090/tcp comment "cockpit"')
    # required part for the script to return to the menu after running its job
    from lib.category_menu import menu
    return menu()