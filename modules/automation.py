def automation():
    print('''
##############################
##  Inside the "automation" folder you have a
##  bunch of Python scripts that can be added as
##  Cronjobs to automate some things
##  There is always an cronjob example inside the files if they
##  were built by the original developer
##  
##  Insite automation folder there is an example for an automated
##  command, carefully read the comments of that file as they
##  explain how to build an automation script and create a cronjob
##  for it, as they work seperatly from this program.
##
##  DO NOT FORGET TO EDIT THESE SCRIPTS FOR YOUR USE CASE/ OS
##############################''')
    try:
        back = int(input('input 0 to go back: '))
        if back == 0:
            from lib.category_menu import menu
            return menu()
        else:
            from lib.category_menu import menu
            print('Incorrect syntax')
            return automation()
    except:
        print('please input a ZERO to go back')
        from lib.category_menu import menu
        return menu()
