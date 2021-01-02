import os

# you can change os.system() for subprocess.run() it should still work

def wireguard_disconnect():
    os.system('sudo wg-quick down wg0')
    # required part for the script to return to the menu after running its job
    from lib.category_menu import menu
    return menu()