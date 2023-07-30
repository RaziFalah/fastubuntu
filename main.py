import time as t
import sys as system
from colorama import Fore, Back, Style
import os
usr = os.getlogin()
#program_virginity check

with open('/home/'+usr+'/fastubuntu/program_virginity.data') as f:
    pv = f.readline()
if(pv == "first_time = true"):
    state = input("Are you willing to provide root access one more time? [Y/n] ")
        print("Processing... Thanks for your trust!")
        t.sleep(3)
        os.system("rm /home/"+usr+"/fastubuntu/program_virginity.data")
        f = open("/home/"+usr+"/fastubuntu/program_virginity.data", "a")
        f.write("first_time = false")
        f.close()
        pass
    elif(state == "n" or state == "N"):
        print("Understandable, goodbye then :)")
        exit()
    else:
        print("Invalid option")
        exit()




if(len(system.argv) == 1):
    print("Preparing...")
    t.sleep(3)
    os.system("sudo apt-get clean")
    os.system("sudo apt-get autoremove")
    os.system("du -sh ~/.cache/thumbnails")
    os.system("rm -r ~/.cache/thumbnails")
    os.system("sudo apt update")
    os.system("sudo apt upgrade")
    os.system("sudo systemctl daemon-reload")
    t.sleep(3)
    os.system("clear")
    print("System was successfuly cleaned!")
    exit()
elif(system.argv[1] == "--allow-logs-cleansing"):
    input("Type anything to confirm [enter]")
    input("We need to be sure again :) [enter]")
    print("Preparing...")
    t.sleep(3)
    os.system("sudo apt-get clean")
    os.system("sudo apt-get autoremove")
    os.system("du -sh ~/.cache/thumbnails")
    os.system("rm -r ~/.cache/thumbnails")
    os.system("sudo apt update")
    os.system("sudo apt upgrade")
    os.system("sudo systemctl daemon-reload")
    os.system("sudo /etc/cron.daily/logrotate")
    os.system("sudo rm -rf /var/log/user.log")
    os.system("sudo rm -rf /var/log/syslog")
    os.system("sudo rm -rf /var/log/messages")
    os.system("sudo journalctl --vacuum-time=0days")
    os.system("sudo systemctl restart syslog.service")
    t.sleep(3)
    os.system("clear")
    print("System was successfuly cleaned!")
    exit()
elif(system.argv[1] == "-h"):
    print("""
    
    fu : clean caches, thumbnail caches, apt caches ;removing unnecessary packages; update & upgrade apt if possible.
    fu [--allow-logs-cleansing] : All the above but also clear [var/logs] (Not recommended for everyone)
    fu [preload] [set/unset] : preload frequencyly used applications
    

    """)
    exit()
elif(len(system.argv) == 3):
  if(system.argv[1] == "preload"):
    if(system.argv[2] == "set"):
        print("ignore unfatal errors!")
        f = open("/home/"+usr+"/sets.data", "a")
        f.write("preload = true")
        f.close()
        os.system("sudo apt install preload")
        exit()
    elif(system.argv[2] == "unset"):
        os.system("rm /home/"+usr+"/fastubuntu/sets.data")
        os.system("sudo apt remove preload")
        exit()
    else:
        print("Unrecognized option!")
        exit()
  else:
    print("Fatal error: unknown option!")
    exit()
else:
    print("Invalid argument, maybe somthing is missing? \nI can tell you what's wrong, but where's the fun in that?")
    exit()







print("No errors were encounterd but program unexpectedly closed with return code (0)")
