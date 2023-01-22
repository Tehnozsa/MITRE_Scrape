import os
from tools.util_func import clearConsole
from parsers.File_Parser import file_parser

def dir_parser(dir,ttp_or_ioc=3):
    # Search for elements that contain the techniques
    parser_table = dict()
    dir_files = (file for file in os.listdir(dir) if os.path.isfile(os.path.join(dir, file)))
    for file in dir_files:
        file_dict = file_parser(dir+file,ttp_or_ioc)
        parser_table.update(file_dict)
        if file_dict == None:
            return ("Not a choice","you must choose the number of an option among those proposed")
    return parser_table

def dir_parser_menu():
    clearConsole()
    directory = input("You choose the dir parser, please enter the dir path (relative from the main.py directory or absolute) :\n")
    if not os.path.isdir(directory): return ("Not a directory","Maybe what you choose was wrong")
    print("1. Parse TTP")
    print("2. Parse IoC")
    print("3. Parse TTP+IoC")    
    choice = input("Choose what you want to parse:\n")
    try:
        choice = int(choice)
    except ValueError:
        return ("Not a choice","you must choose the number of an option among those proposed")
    result = dir_parser(directory,choice)
    input("The raw result is:\n"+str(result))
    return True