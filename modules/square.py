# a simple function that asks for a number and then finds its square
# this works as an example module and how you can create your own 
# its recomended that you stick to the print layout used in here to make the GUI more pleasing
def square() :
    x = int(input('''
    ####################
    ####################
    ##
    ##  give me a number
    ##
    ####################
    ####################
    INPUT: '''))
    print('your number is ' + str(x))
    print('####################')
    y = x * x
    print('####################')
    print('the square of ' + str(x) + ' is ' + str(y))
    print('####################')
    print('####################')
    # required part for the script to return to the menu after running its job
    from lib.category_menu import menu
    return menu()
