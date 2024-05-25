# Boot Manager for YOS Python

# OS SYSTEM IMPORT



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
print("[=======                                 ] 17%")
from os import system
system('clear')

# YOS CLEAR IMPORT
print(" \       /      -----           -----     ")
print("  \     /     /       \        /          ")
print("   \   /     /         \      |           ")
print("    \ /     |           |      \          ")
print("     |      |     -     |       -----     ")
print("     |      |           |            \    ")
print("     |       \         /              |   ")
print("     |        \       /              /    ")
print("     |          -----           -----     ")
print("Importing: YOS/Clear")
print("[==============                          ] 35%")
def clear():
  system('clear')

clear()

# REPLIT DB IMPORT
print(" \       /      -----           -----     ")
print("  \     /     /       \        /          ")
print("   \   /     /         \      |           ")
print("    \ /     |           |      \          ")
print("     |      |     -     |       -----     ")
print("     |      |           |            \    ")
print("     |       \         /              |   ")
print("     |        \       /              /    ")
print("     |          -----           -----     ")
print("Importing: Replit/db")
print("[====================                    ] 50%")
from replit import db

clear()

# PYDICTIONARY IMPORT
print(" \       /      -----           -----     ")
print("  \     /     /       \        /          ")
print("   \   /     /         \      |           ")
print("    \ /     |           |      \          ")
print("     |      |     -     |       -----     ")
print("     |      |           |            \    ")
print("     |       \         /              |   ")
print("     |        \       /              /    ")
print("     |          -----           -----     ")
print("Importing: PyDictionary")
print("[===========================             ] 67%")
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
print("[=================================       ] 83%")
import shutil
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
print("Importing: re")
print("[========================================] 100%")
import re
clear()
  # Imports









# App Variables
# Notpad

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
  print(f'{"YOS Python 0.2beta-3":^{width}}')
  print("")

  # Apps
  print(f'{"Installed Apps":^{width}}')
  print(f'{"-"*int(width):^{width}}')

  print(f'            1. Information{" "*(int(width)-48)}2. Notepad            ')


  # Input
  select = input("Select an app by inputting the corresponding number: ")

  if select == "1":
    dict = PyDictionary()
    def dictionary():
      exec(open("README.md").read())
  elif select == "2":

    clear()
    print("Notepad (Type /exit to exit)")
    print("="*int(width))
    # Check if note is blank

    if db.get("note", "empty") != "empty":
      print(db["note"])
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

home_page()