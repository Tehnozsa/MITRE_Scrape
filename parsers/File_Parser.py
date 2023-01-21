import os
from tools.util_func import clearConsole
from tools.scrape import find_IoC, find_TTP

def file_parser(file,ttp_or_ioc=3):
    # Search for elements that contain the techniques
    parser_table = dict()
    with open(file,"r") as response:
        # 1 == TTP
        if ttp_or_ioc == 1:
            # Make a GET request to the web page and get the lines
            ttps = find_TTP(response.readlines())
            parser_table[file]=ttps
        # 2 == IoC
        elif ttp_or_ioc == 2:
            # Make a GET request to the web page and get the lines
            iocs = find_IoC(response.readlines())
            parser_table[file]=iocs
        # 3 == TTP + IoC
        elif ttp_or_ioc == 3:
            response_lines = response.readlines()
            ttps = find_TTP(response_lines)
            iocs = find_IoC(response_lines)
            parser_table[file]=dict(ttps, **iocs)
        else:
            print("Wrong Choice")
            return None
        return parser_table

def file_parser_menu():
    clearConsole()
    file = input("You choose the file parser, please enter the file path (relative from the main.py directory or absolute) :\n")
    if not os.path.isfile(file): return ("Not a file","Maybe what you choose was wrong")
    print("1. Parse TTP")
    print("2. Parse IoC")
    print("3. Parse TTP+IoC")    
    choice = input("Choose what you want to parse:\n")
    try:
        choice = int(choice)
    except ValueError:
        return ("Not a choice","you must choose the number of an option among those proposed")
    result = file_parser(file,choice)
    input("The raw result is:\n"+str(result))
    return True