import os

# you can change os.system() for subprocess.run() it should still work

def top_all_cores():
    os.system('top -1')
    # required part for the script to return to the menu after running its job
    from categories.monitoring import monitoring
    return monitoring()