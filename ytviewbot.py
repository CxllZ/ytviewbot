import webbrowser
import time
import pyfiglet

ascii_banner = pyfiglet.figlet_format("ViewBot")
print(ascii_banner)
print("					By CxllZ")


url = input("Enter The Link Of The Video: ")
views = input("Enter The Amount Of Views You Want: ")
delay = input("Enter Time For The Next View (atleast 10 secs): ")


print("Be Careful,Your Computer Might Crash Depending On How Many Views You Want!")
print("Ctrl + C To Stop!")

#chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito'

for i in range(int(views)):
    #webbrowser.get(chrome_path).open_new(url)
    webbrowser.visit(url)
    time.sleep(int(delay))
