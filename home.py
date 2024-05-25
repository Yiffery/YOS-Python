# Imports
from replit import db
from os import system
import shutil
import re

def clear():
  system('clear')



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
  print(f'{"YOS Python 0.2 beta":^{width}}')
  print("")
  
  # Apps
  print(f'{"Installed Apps":^{width}}')
  print(f'{"-"*int(width):^{width}}')
  
  print(f'            1. Calculator{" "*(int(width)-48)}2. Notepad            ')
  
  
  # Input
  select = input("Select an app by inputting the corresponding number: ")

  if select == "1":
    print()
  elif select == "2":
    clear()
    print("Notepad (Type /exit to exit, /clear to clear)")
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