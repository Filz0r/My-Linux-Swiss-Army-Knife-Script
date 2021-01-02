from categories.calculator import math
from categories.sys_administration import administration
from categories.wireguard_vpn import wireguard
from categories.monitoring import monitoring

from modules.mining import mining
from modules.automation import automation
from modules.add_alias import add_alias


def menu():
    print('''
##############################
##  0 -> Exit
##  1 -> Math scripts
##  2 -> Linux administration
##  3 -> Wireguard VPN
##  4 -> Mining
##  5 -> Monitoring
##  6 -> Automation
##  7 -> Add an alias to run this script
##############################''')
    question = input('''
##############################
##  What do you want to do? Chose a number:
##############################
INPUT: ''')
    try:
        response = int(question)
        if response == 0:
            print('''
##############################
##############################
##         GOOD BYE         ##
##############################
##############################''')
            import os
            os.system('exit')
        elif response == 1:
            response = 0
            math()
        elif response == 2:
            response = 0
            administration()
        elif response == 3:
            response = 0
            wireguard()
        elif response == 4:
            response = 0
            mining()
        elif response == 5:
            response = 0
            monitoring()
        elif response == 6:
            response = 0
            automation()
        elif response == 7:
            response = 0
            add_alias()
        else:
            print('error invalid choice')
            return menu()

    except:
        print('You need to chose a number')
        return menu()
