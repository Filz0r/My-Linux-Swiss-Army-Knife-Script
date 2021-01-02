#!/usr/bin/env python3

###
# Adding this script to crontab
# IMPORTANT NOTES: 
# - you must run this script as sudo so type "sudo crontab -e" in the console.
# - this script should work without any issues, if you dont create a root cronjob, you must remove the sudo password from the user
# the cronjob is applied to.
# -If you want to build your own scripts do not forget to add the python interperter at the top of each file and change its permissions
# to be ran as an executable file in order for the cronjob below to be able to run.
###
#EXAMPLE CRONJOB:
#                                           (runs everyday at 3AM)
#
#   0 3 * * * /PATH/TO/DIR/linuxSwissArmyKnife/automation/auto_update_upgrade.py >> /PATH/TO/DIR/linuxSwissArmyKnife/logs/update-cron.log 2>&1
#
###

import os

def update():
    os.system('sudo apt update')
    os.system('sudo apt upgrade -y')

update()
