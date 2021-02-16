import webbrowser
import time
import pyfiglet
import os

ascii_banner = pyfiglet.figlet_format("ViewBot")
print(ascii_banner)
print("					By CxllZ")


url = input("Enter The Link Of The Video: ")
views = input("Enter The Amount Of Views You Want: ")
delay = input("Enter How Long To Watch It (atleast 10 secs): ")


print("Be Careful,Your Computer Might Crash Depending On How Many Views You Want!")
print("Ctrl + C To Stop!")


chrome = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito'

for i in range(int(views)):
        webbrowser.get(chrome).open(url)
        time.sleep(int(delay))
