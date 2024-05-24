# Imports
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
  print(f'{"YOS Python 0.1":^{width}}')
  print("")
  
  # Apps
  print(f'{"Installed Apps":^{width}}')
  print(f'{"-"*int(width):^{width}}')
  
  print(f'               1. Calculator{" "*(int(width)-54)}2. Notepad               ')
  
  
  # Input
  select = input("Select an app by inputting the corresponding number: ")

  if select == "1":
    print()
  elif select == "2":
    clear()
    note=""
    print("Notepad (Not saving) (Type /exit to exit)")
    print("="*int(width))
    if note != "":
      print(note)
    else:
      
      while True:
        currentline = input()
        if currentline == "/exit":
          home_page()
        else:
          if note != "":
            note = note + '''
''' + currentline
            print(note)
          else:
            note = currentline
home_page()