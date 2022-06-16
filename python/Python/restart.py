import os

restart = input("do you wish to restart your computer? (Y/N) ")
if restart == 'no':
    exit()
else:
    os.system("shutown /r /t 1")
