import requests
from tools.scrape import find_TTP, find_IoC
from tools.util_func import clearConsole, error

def web_parser(url,ttp_or_ioc=3):
    # Search for elements that contain the techniques
    parser_table = dict()
    response = requests.get(url, verify=False)
    # 1 == TTP
    if ttp_or_ioc == 1:
        # Make a GET request to the web page and get the lines
        ttps = find_TTP(response.iter_lines())
        parser_table[url]=ttps
    # 2 == IoC
    elif ttp_or_ioc == 2:
        # Make a GET request to the web page and get the lines
        iocs = find_IoC(response.iter_lines())
        parser_table[url]=iocs
    # 3 == TTP + IoC
    elif ttp_or_ioc == 3:
        response2 = response
        ttps = find_TTP(response.iter_lines())
        iocs = find_IoC(response2.iter_lines())
        parser_table[url]=dict(ttps, **iocs)
    else:
        print("Wrong Choice")
        return None
    return parser_table

def web_parser_menu():
    clearConsole()
    url = input("You choose the web parser, insert url to parse:\n")
    if "http://" not in url:
        return ("Wrong URL","Maybe add http:// at your URL"),False
    print("1. Parse TTP")
    print("2. Parse IoC")
    print("3. Parse TTP+IoC")    
    choice = input("Choose what you want to parse:\n")
    try:
        choice = int(choice)
    except ValueError:
        return ("Not a choice","you must choose the number of an option among those proposed"),False
    result = web_parser(url,int(choice))
    return result,True