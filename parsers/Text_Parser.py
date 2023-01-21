import os
from tools.util_func import clearConsole
from tools.scrape import find_IoC, find_TTP

def text_parser(text,ttp_or_ioc=3):
    # Search for elements that contain the techniques
    parser_table = dict()
    # 1 == TTP
    if ttp_or_ioc == 1:
        # Make a GET request to the web page and get the lines
        ttps = find_TTP(text.split())
        parser_table[text]=ttps
    # 2 == IoC
    elif ttp_or_ioc == 2:
        # Make a GET request to the web page and get the lines
        iocs = find_IoC(text.split())
        parser_table[text]=iocs
    # 3 == TTP + IoC
    elif ttp_or_ioc == 3:
        response_lines = text.split()
        ttps = find_TTP(response_lines)
        iocs = find_IoC(response_lines)
        parser_table[text]=dict(ttps, **iocs)
    else:
        print("Wrong Choice")
        return None
    return parser_table

def text_parser_menu():
    clearConsole()
    text = input("You choose the text parser, insert text to parse:\n")
    print("1. Parse TTP")
    print("2. Parse IoC")
    print("3. Parse TTP+IoC")    
    choice = input("Choose what you want to parse:\n")
    try:
        choice = int(choice)
    except ValueError:
        return ("Not a choice","you must choose the number of an option among those proposed")
    result = text_parser(text,choice)
    input("The raw result is:\n"+str(result))
    return True