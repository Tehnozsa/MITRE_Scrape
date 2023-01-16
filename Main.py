import os
import sys
from parsers.Web_Parser import web_parser

""" Menu options of the program """
def menu():
    functions = [exit, web_parser_menu, file_parser_menu, dir_parser_menu]
    choice = False
    listChoices = [str(i) for i in range(len(functions))]
    while choice not in listChoices:
        clearConsole()
        print("MITRE/IoC Parser")
        print("---------------------------------------------------------------------\n")
        
        print("1. Parse URL")
        print("2. Parse File")
        print("3. Parse Directory")
        print("0. Exit")

        choice = input("\nChoose your parser: ")
        choice = choice.strip()
    returnValue = functions[int(choice)]()
    if returnValue is not True:
        error(returnValue[0],returnValue[1])
    return True

def web_parser_menu():
    clearConsole()
    url = input("You choose the web parser, insert url to parse:\n")
    if "http://" not in url:
        return error("Wrong URL","Maybe add http:// at your URL")
    print("1. Parse TTP")
    print("2. Parse IoC")
    print("3. Parse TTP+IoC")    
    choice = input("Choose what you want to parse:\n")
    try:
        choice = int(choice)
    except ValueError:
        return error("Not a choice","you must choose the number of an option among those proposed")
    result = web_parser(url,int(choice))
    if result == None:
        back()
        return True
    input(result)
    return True

def file_parser_menu():
    clearConsole()
    file = input("You choose the file parser, insert file to parse:\n")
    if not os.path.isfile(file): return error("Not a file","Maybe what you choose was wrong")
    print("1. Parse TTP")
    print("2. Parse IoC")
    print("3. Parse TTP+IoC")    
    choice = input("Choose what you want to parse:\n")
    try:
        choice = int(choice)
    except ValueError:
        return error("Not a choice","you must choose the number of an option among those proposed")
    result = web_parser(file,choice)
    if result == None: return False
    input(result)
    return True

def dir_parser_menu():
    clearConsole()
    directory = input("You choose the dir parser, insert dir to parse:\n")
    if not os.path.isdir(directory): return error("Not a directory","Maybe what you choose was wrong")
    print("1. Parse TTP")
    print("2. Parse IoC")
    print("3. Parse TTP+IoC")    
    choice = input("Choose what you want to parse:\n")
    try:
        choice = int(choice)
    except ValueError:
        return error("Not a choice","you must choose the number of an option among those proposed")
    result = web_parser(directory,choice)
    if result == None: 
        print("No result on "+directory)
        return back()
    input(result)
    return True

""" Function that prints the program logo """
def logo():
    logo_ascii = """ 
    __  _________________  ______   ______      ______   ____                           
   /  |/  /  _/_  __/ __ \/ ____/ _/_/  _/___  / ____/  / __ \____ ______________  _____
  / /|_/ // /  / / / /_/ / __/  _/_/ / // __ \/ /      / /_/ / __ `/ ___/ ___/ _ \/ ___/
 / /  / // /  / / / _, _/ /____/_/ _/ // /_/ / /___   / ____/ /_/ / /  (__  )  __/ /    
/_/  /_/___/ /_/ /_/ |_/_____/_/  /___/\____/\____/  /_/    \__,_/_/  /____/\___/_/     """
    print(logo_ascii)
    print("---------------------------------------------------------------------\n")

""" Function that cleans the console screen """
clearConsole = lambda: os.system('cls' if os.name in ('nt','dos') else 'clear') or logo()

def back():
    input("Press ENTER to return to the menu")

def exit():
	""" Function that prints an exit message """
	clearConsole()
	print("See you soon!\n")
	sys.exit()

def error(cause="Unknown",mitigation="Unknown"):
	""" Function that prints the cause and its mitigation for an error """
	clearConsole()
	print("Error")
	print("Cause: "+cause)
	print("Mitigation: "+mitigation)
	print("If the error persists, please make a request on GitHub.")
	input("\nPress ENTER to return to the menu")
	return True

def main():
    menuResponse = True
    while menuResponse:
        menuResponse = menu()

if __name__ == '__main__':
	main()