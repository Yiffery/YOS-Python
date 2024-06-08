yosversion = "0.6beta-f1"
print("Initializing...")
def yosloading(mode, text, current, total):
  equals = "="*round(int(current) / int(total) * 40)
  empties = " " * (40-int(round(current/total * 40)))
  percent = str(current/total*100)
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
  print("{0}: {1}".format(mode, text))
  print("["+equals+empties+"] "+percent+"%")

yosloading("Loading", "os/system", 1, 8)
from os import system
system('clear')
yosloading("Importing", "sys", 2, 8)
import sys
system('clear')
yosloading("Importing", "re", 3, 8)
import re
system('clear')
yosloading("Importing", "replit/db", 4, 8)
from replit import db
system('clear')
yosloading("Importing", "shutil", 5, 8)
import shutil
system('clear')
yosloading("Importing", "random", 6, 8)
import random
system('clear')
yosloading("Importing", "time", 7, 8)
import time
system('clear')
yosloading("Importing", "YOSAPIs", 8, 8)
dimensions = re.findall(r'\b\d+\b', str(shutil.get_terminal_size()))
width = int(dimensions[0])
height = int(dimensions[1])
def clear():
  system('clear')
def titlebar(app, page):
  print("{0} ({1})".format(app, page))
  print("="*int(width))

clear()
print("Loading YOS...")
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
  # Print Title and Subtitle
  print(f'{"YOS Python {0}":^{width}}'.format(yosversion))
  print("")
  # Apps
  print(f'{"Installed Apps":^{width}}')
  print(f'{"-"*int(width):^{width}}')
  print(f'{"1. Settings     2. Notepad":^{width}}')
  print(f'{"3. Power Options     4. YDocs":^{width}}')
  print(f'{"5. Calculator":^{width}}')
  # Input
  select = input("Select an app by inputting the corresponding number: ")
  if select == "1":
    def settings():
      clear()
      titlebar("Settings", "Home")
      print("1. About")
      print("2. Reset")
      settings_open = input("Enter the number of the setting you want to open: ")
      if settings_open == "1":
        def about():
          clear()
          titlebar("Settings", "About")
          print("YOS Python")
          print("-"*int(width))
          print("YOS Python Version {}" .format(yosversion))
          print("YOS Python is open-source at https://github.com/yiffery/YOS-Python")
          print("YOS Python has a website at https://yiffery.github.io/YOS-Python")
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
          titlebar("Settings", "Reset")
          resetchoice = input("Are you sure you want to factory reset? (Y/N)")
          if resetchoice == "Yes" or "yes" or "y" or "Y":
            clear()
            titlebar("Settings", "Resetting...")
            yos_logo()
            print("Resetting: YDocs")
            for count in range(1, len(db.prefix("text")) + 1):
              print("Deleting: " + "Document " + str(count))
              del db["text" + str(count)]
            home_page()
        reset()
      if settings_open == "/exit":
        home_page()
      else:
        clear()
        titlebar("Settings", "Error")
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
      poweroption = input("Select an option by inputting the corresponding number: ")
      if poweroption == "1":
        yos_logo()
        print("Shutting Down...")
      elif poweroption == "2":
        yos_logo()
        print("Restarting...")
        exec(open("main.py").read())
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
      for count in range(1, len(db.prefix("text")) + 1):
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
  elif select == "5":
    def calculator():
      clear()
      titlebar("Calculator", "Home")
      print('''1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Random Number Generator''')
      calcinput = input("Choose an option by inputting the corresponding number: ")
      if calcinput == "1":
        clear()
        titlebar("Calculator", "Addition")
        firstnumber = int(input("Enter the first number: "))
        secondnumber = int(input("Enter the second number: "))
        print("Answer: " + str(firstnumber+secondnumber))
        input("Press enter to continue")
        calculator()
      elif calcinput == "2":
        clear()
        titlebar("Calculator", "Subtraction")
        firstnumber = int(input("Enter the first number: "))
        secondnumber = int(input("Enter the second number: "))
        print("Answer: " + str(firstnumber-secondnumber))
        input("Press enter to continue")
        calculator()
      elif calcinput == "3":
        clear()
        titlebar("Calculator", "Multiplication")
        firstnumber = int(input("Enter the first number: "))
        secondnumber = int(input("Enter the second number: "))
        print("Answer: " + str(firstnumber*secondnumber))
        input("Press enter to continue")
        calculator()
      elif calcinput == "4":
        clear()
        titlebar("Calculator", "Division")
        firstnumber = int(input("Enter the first number: "))
        secondnumber = int(input("Enter the second number: "))
        print("Answer: " + str(firstnumber/secondnumber))
        input("Press enter to continue")
        calculator()
      elif calcinput == "5":
        clear()
        titlebar("Calculator", "Random Number Generator")
        firstnumber = int(input("Enter the lower range: "))
        secondnumber = int(input("Enter the upper range: "))
        print("Answer: "+str(random.randint(firstnumber, secondnumber)))
        input("Press enter to cotinue")
        calculator()
      elif calcinput == "/exit":
        home_page()
      else:
        clear()
        titlebar("Calculator", "Error")
        print("Not an option!")
        time.sleep(1)
        calculator()
    calculator()
  else:
    print("Invalid App")
    time.sleep(0.5)
    home_page()
home_page()