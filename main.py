yosversion = "0.6beta-0"
print(" \       /      -----           -----     ")
print("  \     /     /       \        /          ")
print("   \   /     /         \      |           ")
print("    \ /     |           |      \          ")
print("     |      |     -     |       -----     ")
print("     |      |           |            \    ")
print("     |       \         /              |   ")
print("     |        \       /              /    ")
print("     |          -----           -----     ")
print("                                          ")
print("Importing: os/System")
print("[=====                                   ] 13%")
from os import system
import sys
system('clear')
print(" \       /      -----           -----     ")
print("  \     /     /       \        /          ")
print("   \   /     /         \      |           ")
print("    \ /     |           |      \          ")
print("     |      |     \     |       -----     ")
print("     |      |           |            \    ")
print("     |       \         /              |   ")
print("     |        \       /              /    ")
print("     |          -----           -----     ")
print("Importing: YOS/Clear")
print("[==========                              ] 25%")
def clear():
  system('clear')
clear()
print(" \       /      -----           -----     ")
print("  \     /     /       \        /          ")
print("   \   /     /         \      |           ")
print("    \ /     |           |      \          ")
print("     |      |     |     |       -----     ")
print("     |      |           |            \    ")
print("     |       \         /              |   ")
print("     |        \       /              /    ")
print("     |          -----           -----     ")
print("Importing: Replit/db")
print("[===============                         ] 38%")
from replit import db
clear()
print(" \       /      -----           -----     ")
print("  \     /     /       \        /          ")
print("   \   /     /         \      |           ")
print("    \ /     |           |      \          ")
print("     |      |     /     |       -----     ")
print("     |      |           |            \    ")
print("     |       \         /              |   ")
print("     |        \       /              /    ")
print("     |          -----           -----     ")
print("Importing: colorama")
print("[====================                    ] 50%")
from colorama import Fore, Back, Style
clear()
print(" \       /      -----           -----     ")
print("  \     /     /       \        /          ")
print("   \   /     /         \      |           ")
print("    \ /     |           |      \          ")
print("     |      |     -     |       -----     ")
print("     |      |           |            \    ")
print("     |       \         /              |   ")
print("     |        \       /              /    ")
print("     |          -----           -----     ")
print("Importing: Shutil")
print("[==========================              ] 63%")
import shutil
clear()
print(" \       /      -----           -----     ")
print("  \     /     /       \        /          ")
print("   \   /     /         \      |           ")
print("    \ /     |           |      \          ")
print("     |      |     \     |       -----     ")
print("     |      |           |            \    ")
print("     |       \         /              |   ")
print("     |        \       /              /    ")
print("     |          -----           -----     ")
print("Importing: re")
print("[==============================          ] 75%")
import re
clear()
print(" \       /      -----           -----     ")
print("  \     /     /       \        /          ")
print("   \   /     /         \      |           ")
print("    \ /     |           |      \          ")
print("     |      |     |     |       -----     ")
print("     |      |           |            \    ")
print("     |       \         /              |   ")
print("     |        \       /              /    ")
print("     |          -----           -----     ")
print("Importing: platform")
print("[===================================     ] 88%")
import platform
clear()
print(" \       /      -----           -----     ")
print("  \     /     /       \        /          ")
print("   \   /     /         \      |           ")
print("    \ /     |           |      \          ")
print("     |      |     /     |       -----     ")
print("     |      |           |            \    ")
print("     |       \         /              |   ")
print("     |        \       /              /    ")
print("     |          -----           -----     ")
print("Importing: time")
print("[========================================] 100%")
import time
clear()
def yos_logo():
  print(" \       /      -----           -----     ")
  print("  \     /     /       \        /          ")
  print("   \   /     /         \      |           ")
  print("    \ /     |           |      \          ")
  print("     |      |     -     |       -----     ")
  print("     |      |           |            \    ")
  print("     |       \         /              |   ")
  print("     |        \       /              /    ")
  print("     |          -----           -----     ")
  print("                                          ")
note = "" 
# Get terminal size
dimensions = re.findall(r'\b\d+\b', str(shutil.get_terminal_size()))
width = dimensions[0]
def home_page():
  clear()
  # Get terminal size
  dimensions = re.findall(r'\b\d+\b', str(shutil.get_terminal_size()))
  width = dimensions[0]
  height = dimensions[1]
  # Print Title and Subtitle
  print(f'{"YOS Python {0}":^{width}}'.format(yosversion))
  print("")
  # Apps
  print(f'{"Installed Apps":^{width}}')
  print(f'{"-"*int(width):^{width}}')
  print(f'{"1. Settings     2. Notepad":^{width}}')
  print(f'{"3. Power Options     4. YDocs":^{width}}')
  # Input
  select = input("Select an app by inputting the corresponding number: ")
  if select == "1":
    def settings_titlebar(page):
      print("Settings (Type /exit to exit, 0 for back) ({})".format(page))
      print("="*int(width))
    def settings():
      clear()
      settings_titlebar("Home")
      print("1. About")
      settings_open = input("Enter the number of the setting you want to open: ")
      if settings_open == "1":
        def about():
          clear()
          settings_titlebar("About")
          print("YOS Python")
          print("-"*int(width))
          print("YOS Python Version {}" .format(yosversion))
          print("YOS Python is open-source at https://github.com/yiffery/YOS-Python")
          print("YOS Python has a website at https://github.io/yiffery/YOS-Python")
          print()
          print("Console")
          print("-"*int(width))
          print("Console width: " + str(width))
          print("Console height: " + str(height))
          print()
          print("Python")
          print("-"*int(width))
          print("Python Version: " + sys.version)
          print()
          print("Dependencies")
          print("-"*int(width))
          print("os/system")
          print("sys")
          print("Replit/db")
          print("colorama")
          print("Shutil")
          print("re")
          print("platform")
          print("time")
          input("Hit enter to go back")
          settings()
        about()
      if settings_open == "2":
        def reset():
          clear()
          settings_titlebar("Reset")
          resetchoice = input("Are you sure you want to reset your settings? (Y/N)")
          if resetchoice
          
      if settings_open == "/exit":
        home_page()
      else:
        clear()
        settings_titlebar("Error")
        print("Not an option!")
        time.sleep(1)
        settings()
    settings()
  elif select == "2":
    def notepad():
      clear()
      print("Notepad (Type /exit to exit) (Type /clear to clear")
      print("="*int(width))
      # Check if note is blank
      if db.get("note", "empty") != "empty":
        print(db["note"])
        while True:
          currentline = input()
          # Check if note is blank
          if currentline == "/exit":
            home_page()
          elif currentline == "/clear":
            db["note"] = ""
            notepad()
          else:
            if db.get("note", "empty") != "empty":
              # If note isn't blank, create new line and write
              db["note"] = db["note"] + '''
          ''' + currentline
            else:
              # If note is blank, don't create new line, but write
              db["note"] = currentline
      else:
        while True:
          currentline = input()
          # Check if note is blank
          if currentline == "/exit":
            home_page()
  
          else:
            if db.get("note", "empty") != "empty":
              # If note isn't blank, create new line and write
              db["note"] = db["note"] + '''
          ''' + currentline
            else:
              # If note is blank, don't create new line, but write
              db["note"] = currentline
    notepad()
  elif select == "3":
    def power_options():
      clear()
      print("Notepad (Type /exit to exit)")
      print("="*int(width))
      print("1. Power off")
      print("2. Restart")
      print("3. Reset")
      poweroption = input("Select an option by inputting the corresponding number: ")
      if poweroption == "1":
        yos_logo()
        print("Shutting Down...")
      elif poweroption == "2":
        yos_logo()
        print("Restarting...")
        exec(open("main.py").read())
      elif poweroption == "3":
        sure = input("Are you sure you want to reset? (Y/N): ")
        if sure == "Y" or "Yes" or "yes":
          yos_logo()
          print("Resetting...")
          db["note"] = ""
          clear()
          yos_logo()
          print("YOS has been reset")
          time.sleep(1)
          exec(open("main.py").read())
        if sure == "N" or "No" or "no":
          home_page()
      elif poweroption == "/exit":
        home_page()
      else:
        print("{} was not an option".format(poweroption))
        time.sleep(1)
        power_options()
    power_options()
  elif select == "4":
    def remove_last_line_from_string(s):
      return s[:s.rfind('\n')]
    def YDocsTitle():
      print("YDocs (Type /exit to exit)")
      print("="*int(width))
    def YDocs():
      number_of_documents = 0
      clear()
      YDocsTitle()
      # Check how many documents are stored in replit DB
      for count in range(1, len(db.prefix("name")) + 1):
        print("Document {}".format(count))
        number_of_documents = number_of_documents + 1
      docselect = input("Which document would you like to open? (0 for new)")
      if int(docselect) <= number_of_documents and int(docselect) != 0:
        clear()
        YDocsTitle()
        print("Opening document {0}".format(docselect))
        clear()
        YDocsTitle()
        # print document contents from replit db
        while True:
          clear()
          YDocsTitle()
          text = db["text{0}".format(docselect)]
          print(text)
          entertext = input()
          if entertext == "/dl":
            db["text{0}".format(docselect)] = remove_last_line_from_string(text)
          elif entertext == "/rename":
            clear()
            YDocsTitle()
            db["name{0}".format(docselect)] = input("Enter new name: ")
          elif entertext == "/exit":
            db["text{0}".format(docselect)] = remove_last_line_from_string(text)
            home_page()
          else:
            db["text{0}".format(docselect)] = text + "\n" + entertext
      elif int(docselect) == 0:
        number_of_documents += 1
        docselect = number_of_documents
        db["text{0}".format(docselect)] = ""
        while True:
          clear()
          YDocsTitle()
          text = db["text{0}".format(docselect)]
          print(text)
          entertext = input()
          if entertext == "/dl":
            db["text{0}".format(docselect)] = remove_last_line_from_string(text)
          elif entertext == "/rename":
            clear()
            YDocsTitle()
            db["name{0}".format(docselect)] = input("Enter new name: ")
          elif entertext == "/exit":
            db["text{0}".format(docselect)] = remove_last_line_from_string(text)
            home_page()
          else:
            if db["text{0}".format(docselect)] == "":
              db["text{0}".format(docselect)] = text + entertext
            else:
              db["text{0}".format(docselect)] = text + "\n" + entertext
    YDocs()
  else:
    print("Invalid App")
    time.sleep(0.5)
    home_page()
home_page()