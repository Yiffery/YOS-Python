# Beta controlled tests
yosversion = "0.4beta-3"
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
print("Importing: pyautogui: typewrite")
print("[====================                    ] 50%")

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

  print(f'{"1. Information     2. Notepad":^{width}}')
  print(f'{"3. Power Options     4. YDocs":^{width}}')
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
      input("Press enter to continue")
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
        print("Document {0}: {1}".format(count, db.prefix("name")[count - 1]))
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
        newdocname = input("What would you like to name your new document?")
        db["name{0}".format(number_of_documents+1)] = newdocname
        number_of_documents += 1
        docselect = number_of_documents
        while True:
          print(docselect)
          YDocsTitle()
          
          if db["text{0}".format(docselect)]:
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
        
    YDocs()
  else:
    print("Invalid App")
    time.sleep(0.5)
    home_page()
home_page()