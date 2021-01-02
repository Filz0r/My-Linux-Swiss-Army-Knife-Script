import os

# you can change os.system() for subprocess.run() it should still work

def wireguard_check():
    os.system('sudo wg')
    print('if you saw nothing but this you are not connected to your vpn server')
    # required part for the script to return to the menu after running its job
    from lib.category_menu import menu
    return menu()