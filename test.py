import subprocess

username = input('What is the username on your system?(case sensitive): ')
# alias = "armyknife='/home/{}/My-Linux-Swiss-Army-Knife-Script/myLinuxSwissArmyKnife.py'".format(
#    username)
#bash_path = "/home/{}/.bashrc".format(username)
#subprocess.run(['echo alias ' + alias + ' >> ' + bash_path])
program_path = "/home/{}/Documents/DEV/My-Linux-Swiss-Army-Knife-Script/myLinuxSwissArmyKnife.py".format(
    username)
subprocess.run(['sudo', 'ln', '-s', program_path, '/usr/bin/armyknife'])
