import os

# you can change os.system() for subprocess.run() it should still work

def wireguard_watch():
    print('if you only see this message you are not connected to your vpn server')
    print('PRESS CTRL + C to exit')
    os.system('watch -n 1 sudo wg')
    # required part for the script to return to the menu after running its job
    from categories.monitoring import monitoring
    return monitoring()