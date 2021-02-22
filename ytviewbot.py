import webbrowser
import time
import pyfiglet
import platform
import os

ascii_banner = pyfiglet.figlet_format("ViewBot")
print(ascii_banner)
print("					By CxllZ")


url = input("Enter The Link Of The Video: ")
views = input("Enter The Amount Of Views You Want: ")
delay = input("Enter Minimum Time To Watch (seconds): ")
brow = input("Enter Your Default Browser : ")

print("")
print("Is The Following Details Correct?")
print("")
print("url:",url)
print("views:",views)
print("Watch Time:",delay,"seconds")
print("browser:",brow)
print("")

chrome_win = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito'


while True:
    correct = input("y/n: ")
    if correct == '' or not correct in ['y','n']: 
        print('Please answer with y or n!') 
    else: 
        break
    
if correct == 'y':
    for i in range(int(views)):
            if platform.system() == 'Windows':
                print("Successfully Viwed. ")
                os.system(" killall -9 " + brow)
                webbrowser.get(chrome_win).open(url)
                time.sleep(int(minimum))
            else:
                print("Successfully Viwed. ")
                os.system("taskkill /im",brow,"/")
                webbrowser.open(url)
                time.sleep(int(minimum))
if correct == 'n':
    print("RESTARTING...")
    os.execv(sys.executable, ['python'] + sys.argv)
