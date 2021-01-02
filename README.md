# My-Linux-Swiss-Army-Knife-Script
  This is my first ever Python Script that is compressed in a bunch of small scripts that run with the help of a simple GUI, I use it to automate some tedious tasks on my everyday actions inside a command line, hope this serves as an inspiration for you to build yours!
  
## How to use
  1-  Run the following command in your command line 
      `git clone https://github.com/Filz0r/My-Linux-Swiss-Army-Knife-Script.git`
  2-  Go into the folder you just downloaded and run the following command:
      `chmod x+ myLinuxSwissArmyKnife.py`
  3-  Make sure you have Python3 installed in your system!
  4-  after that you can run this script by running one of the following commands:
      `/Path/To/Dir/myLinuxSwissArmyKnife.py`
      OR
      `cd /Path/To/Dir/`
      `./myLinuxSwissArmyKnife.py`
## Important Notes

This tool is not built to be used by everyone, however it was designed to be able to easily be changed by anyone that knows Python, I'm no Python guru as it stands, this is in fact my first ever Python project.

When you download this project inside its folder you have 4 directories, **automation, categories, lib and modules**.
- The **lib** folder is where all the essential modules for the program to work, right now you only have the category_menu.py script in there as this is still a really barebones program, but as time goes by I want to build an actual GUI for this program, and this is where these files will probably live.
- **modules** is where all the magic happens, the files stored in there are simple scripts that automate my tasks when setting up an new Linux server for example, I can use the scripts I have in the **System Administration** category to change the initial configuration of a fresh install of linux, like setting host files, downloading and configuring UFW and so on. Essentially a module is the tiny program that runs a task and then returns to the main menu after running said task.
- Inside **automation** is where you can create automation scripts that can be added as cronjobs in your Linux systems, in the provided example (auto_update_upgrade.py) I built a pretty good example that after implemented will update and upgrade any software every day at 3 AM.
- The **categories** folder is where you create your own sub-menus for your workloads, you need to implement one of these files if you for example have various modules for one specific category, for example I use a Wireguard VPN in order to access my home network on the go, so I built a category for my **client** pc, I can easly use this script to connect, disconnect to my Wireguard VPN and I can also use it to check my connection to it, there is no Linux GUI for connecting to a Wireguard VPN so I thought of automating the commands that are required to connect to a Wireguard VPN in this script as an easy solution!

This project will keep on growing as I learn more and more about Phyton, if you feel like sharing any tips on how to improve this script feel, or even help me building this into a app that everyone can use free to contact me!
