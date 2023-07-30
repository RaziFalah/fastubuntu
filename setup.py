import os
import time as t
from colorama import Fore, Back, Style
usr = os.getlogin()

state = input("Would you like to install fast ubuntu [Y/n]? ")
if (state == "Y" or state == "y"):
    pass
elif (state == "n" or state == "N"):
    print("Aborted by user!")
    exit()
else:
    print("invalid option")
    exit()

state = input("Are you willing to provide root access one more time? [Y/n] ")
if(state == "y" or state == "Y"):
        print("Processing... Thanks for your trust! Again")
        t.sleep(3)
        os.system("sudo chmod -R a+rwx /home/"+usr+"/fastubuntu")
        f = open("/home/"+usr+"/fastubuntu/program_virginity.data", "a")
        f.write("first_time = true")
        f.close()
        pass
elif(state == "n" or state == "N"):
        print("Understandable, goodbye then :)")
        exit()
else:
        print("Invalid option")
        exit()

print("Recognizing user...")
t.sleep(3)

print("Setting up command line interface... [fu]")
f = open("/home/"+usr+"/.bashrc", "a")
f.write("alias fu='python3 /home/"+usr+"/fastubuntu/main.py'")
f.close()
t.sleep(3)
print("Reinitializing session configuration ...")
t.sleep(3)



print(Fore.YELLOW + "FU: User was logged into a new session, if exited to previous session program will not work!")
os.system("exec bash --login")
