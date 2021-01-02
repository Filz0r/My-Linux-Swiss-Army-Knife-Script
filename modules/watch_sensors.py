import os

# you can change os.system() for subprocess.run() it should still work

def watch_sensors():
    os.system('watch -n 1 sensors')
    # required part for the script to return to the menu after running its job
    from categories.monitoring import monitoring
    return monitoring()