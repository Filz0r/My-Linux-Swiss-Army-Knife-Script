import os

# you can change os.system() for subprocess.run() it should still work

def hosts():
   print('''
##############################
##  
##  opening /etc/hosts file, you need sudo rights!
##
##############################''')
   os.system('sudo nano /etc/hosts')
   # required part for the script to return to the menu after running its job
   from lib.category_menu import menu
   return menu()
