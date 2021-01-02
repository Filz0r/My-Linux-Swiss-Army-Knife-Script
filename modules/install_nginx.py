import os

# you can change os.system() for subprocess.run() it should still work

def install_nginx():
    print('''
##############################
##  
##    -> THIS SCRIPT REQUIRES SUDO
##
##  This script installs NGINX on the server
##  Enables and starts it
##  And adds ports 80 and 443 as an exception to UFW
##
##############################''')
    os.system('sudo apt install nginx -y')
    os.system('sudo systemctl enable nginx')
    os.system('sudo systemctl start nginx')
    os.system('sudo ufw allow http')
    os.system('sudo ufw allow https')
    # required part for the script to return to the menu after running its job
    from lib.category_menu import menu
    return menu()