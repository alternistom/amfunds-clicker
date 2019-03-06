import pyautogui
import pyperclip
import time

# v1.0 initial release

print( """

 █████╗ ███╗   ███╗███████╗██████╗ ██╗ ██████╗ █████╗ ███╗   ██╗
██╔══██╗████╗ ████║██╔════╝██╔══██╗██║██╔════╝██╔══██╗████╗  ██║
███████║██╔████╔██║█████╗  ██████╔╝██║██║     ███████║██╔██╗ ██║
██╔══██║██║╚██╔╝██║██╔══╝  ██╔══██╗██║██║     ██╔══██║██║╚██╗██║
██║  ██║██║ ╚═╝ ██║███████╗██║  ██║██║╚██████╗██║  ██║██║ ╚████║
╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
                                                                
███████╗██╗   ██╗███╗   ██╗██████╗ ███████╗                     
██╔════╝██║   ██║████╗  ██║██╔══██╗██╔════╝                     
█████╗  ██║   ██║██╔██╗ ██║██║  ██║███████╗                     
██╔══╝  ██║   ██║██║╚██╗██║██║  ██║╚════██║                     
██║     ╚██████╔╝██║ ╚████║██████╔╝███████║                     
╚═╝      ╚═════╝ ╚═╝  ╚═══╝╚═════╝ ╚══════╝                     
                                                                
 ██████╗██╗     ██╗ ██████╗██╗  ██╗███████╗██████╗              
██╔════╝██║     ██║██╔════╝██║ ██╔╝██╔════╝██╔══██╗             
██║     ██║     ██║██║     █████╔╝ █████╗  ██████╔╝             
██║     ██║     ██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗             
╚██████╗███████╗██║╚██████╗██║  ██╗███████╗██║  ██║             
 ╚═════╝╚══════╝╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝  
 
 v.1.0 by tamas.fabian@dealogic.com
 last updated on:      Mar-06-2019
 initially created on: Mar-06-2019
 
╔────────────────────────────ATTENTION!─────────────────────────────╖
║ Make sure the script window is on the right screen and on the left║
║ the first page of the proEDGAR is opened up with 100% zoom.       ║
╚────────────────────────────ATTENTION!─────────────────────────────╜
 
""")


tobefilename = input("► What should we name out txt file? ")
totalfilings = input("► How many total filings this month? ")

pages = int(totalfilings) // 15
actualpages = pages + 1

filename = tobefilename + ".txt"
f = open(filename, "a", encoding="utf-8")

pyautogui.click(503, 1011) #activates proEDGAR window

print("")
print("Please don't touch ANYTHING on your computer till you are prompted to do so!")
print("")

for _ in range(int(actualpages)):
	pyautogui.hotkey("ctrl", "a")
	pyautogui.hotkey("ctrl", "c")
	page_data = pyperclip.paste()
	f.write((str(page_data)) + "\n")
	actualpages = actualpages - 1
	x, y = pyautogui.locateCenterOnScreen('amnext.png')
	#pyautogui.click(1448, 592)
	pyautogui.click(x, y)
	time.sleep(3)
	print("Page appended to txt file.")
	
print("")
print("File SAVED. Now exiting...")
print("")

f.close()