yosversion = "0.3beta-2"
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
system('clear')
# YOS CLEAR IMPORT
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
# REPLIT DB IMPORT
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
# PYDICTIONARY IMPORT
print(" \       /      -----           -----     ")
print("  \     /     /       \        /          ")
print("   \   /     /         \      |           ")
print("    \ /     |           |      \          ")
print("     |      |     /     |       -----     ")
print("     |      |           |            \    ")
print("     |       \         /              |   ")
print("     |        \       /              /    ")
print("     |          -----           -----     ")
print("Importing: PyDictionary")
print("[====================                    ] 50%")
from PyDictionary import PyDictionary
clear()
# SHUTIL IMPORT
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
print("[=================================       ] 63%")
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
print("[========================================] 75%")
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
print("[========================================] 88%")
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
  # CLEAR IT ALL!
  clear()
  # Get terminal size
  dimensions = re.findall(r'\b\d+\b', str(shutil.get_terminal_size()))
  width = dimensions[0]
  # Print Title and Subtitle

  print(f'{"YOS Python {0}":^{width}}'.format(yosversion))
  print("")

  # Apps
  print(f'{"Installed Apps":^{width}}')
  print(f'{"-"*int(width):^{width}}')

  print(f'            1. Information{" "*(int(width)-48)}2. Notepad            ')
  print(f'{"3. Power Options":^{width}}')
  # Input
  select = input("Select an app by inputting the corresponding number: ")

  if select == "1":
    def information():
      clear()
      print("Information (Type /exit to exit)")
      print("="*int(width))
      print("Python Info:")
      print("Current Python Version: {0}".format(platform.python_version()))
      print()
      print("YOS Info")
      print("Current YOS Version: {0}".format(yosversion))
      print()
      print("Installed Apps:")
      print("1. Information")
      print("2. Notepad")
      exit = input("Press enter to continue")
      home_page()
    information()
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
      print("Notepad (Type /exit to exit) (Type /clear to clear")
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
          exec(open("main.py").read())
    power_options()
  else:
    print("Invalid App")
    time.sleep(0.5)
    home_page()
home_page()