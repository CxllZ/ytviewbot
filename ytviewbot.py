import webbrowser
import time
import pyfiglet
import platform

ascii_banner = pyfiglet.figlet_format("ViewBot")
print(ascii_banner)
print("					By CxllZ")


url = input("Enter The Link Of The Video: ")
views = input("Enter The Amount Of Views You Want: ")
delay = input("Enter How Long To Watch It (atleast 10 secs): ")

print("")
print("Next Video In",delay,"Seconds And Giving",views,"views")
print("Be Careful,Your Computer Might Crash Depending On How Many Views You Want!")
print("Ctrl + C To Stop!")


chrome_win = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito'


for i in range(int(views)):
        
        if platform.system() == 'Windows':
                webbrowser.get(chrome_win).open(url)
                time.sleep(int(delay))
        else:
                webbrowser.open(url)
                time.sleep(int(delay))
