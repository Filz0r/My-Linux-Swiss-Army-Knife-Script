from modules.square import square


def math():
    print('''
##############################
##  0 -> Go back
##  1 -> Find the square of a number
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
            square()
        else:
            print('error invalid choice')
    except:
        print('You need to chose a number')
