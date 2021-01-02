from modules.wireguard_check import wireguard_check
from modules.wireguard_connect import wireguard_connect
from modules.wireguard_disconnect import wireguard_disconnect

def wireguard():
    print('''
##############################
##  0 -> Go back
##  1 -> Check/monitor wireguard connection
##  2 -> Connect to Wireguard VPN
##  3 -> Disconnect to Wireguard VPN
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
            wireguard_check()
        elif response == 2:
            response = 0
            wireguard_connect()
        elif response == 3:
            response = 0
            wireguard_disconnect()
        else:
            print('error invalid choice')
    except:
        print('You need to chose a number')