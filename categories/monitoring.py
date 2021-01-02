from modules.wireguard_watch import wireguard_watch
from modules.watch_gpu import watch_gpu
from modules.watch_sensors import watch_sensors
from modules.top_all_cores import top_all_cores


def monitoring():
    print('''
##############################
##  0 -> Go back
##  1 -> Watch GPU
##  2 -> top (all cores)
##  3 -> watch sensors
##  4 -> watch wireguard connection
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
            watch_gpu()
        elif response == 2:
            response = 0
            top_all_cores()
        elif response == 3:
            response = 0
            watch_sensors()
        elif response == 4:
            response = 0
            wireguard_watch()
        else:
            print('error invalid choice')
    except:
        print('You need to chose a number')
