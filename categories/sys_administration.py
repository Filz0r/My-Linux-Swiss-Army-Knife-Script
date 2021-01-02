from modules.hosts import hosts
from modules.update import update
from modules.ufw_basic import ufw_basic
from modules.install_cockpit import install_cockpit
from modules.install_nginx import install_nginx
from modules.sshd_config import sshd_config


def administration():
    print('''
##############################
##  0 -> Go back
##  1 -> Update system
##  2 -> Update hosts file
##  3 -> Install and setup ufw (SERVER ONLY)
##  4 -> Install cockpit
##  5 -> Install nginx
##  6 -> Edit sshd_config file
##############################''')
    question = input('''
##############################
##  What do you want to do? Chose a number:
##############################
INPUT: ''')
    try:
        response = int(question)
        if response == 0:
            response = 0
            from lib.category_menu import menu
            menu()
        elif response == 1:
            response = 0
            update()
        elif response == 2:
            response = 0
            hosts()
        elif response == 3:
            response = 0
            ufw_basic()
        elif response == 4:
            response = 0
            install_cockpit()
        elif response == 5:
            response = 0
            install_nginx()
        elif response == 6:
            response = 0
            sshd_config()
        else:
            print('error invalid choice')
    except:
        print('You need to chose a number')
