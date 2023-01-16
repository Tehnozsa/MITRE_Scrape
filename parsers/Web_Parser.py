import requests, re
from tools.scrape import find_TTP, find_IoC

def web_parser(url,choice=3):
    ttp_or_ioc = choice
    # Search for elements that contain the techniques
    parser_table = dict()
    # 1 == TTP
    if ttp_or_ioc == 1:
        # Make a GET request to the web page and get the lines
        response = requests.get(url, verify=False)
        ttps = find_TTP(response.iter_lines())
        if ttps['TTP'] == []:
            print("No result on "+url)
            return None
        parser_table[url]=ttps
    # 2 == IoC
    elif ttp_or_ioc == 2:
        # Make a GET request to the web page and get the lines
        response = requests.get(url, verify=False)
        iocs = find_IoC(response.iter_lines())
        parser_table[url]=iocs
    # 3 == TTP + IoC
    elif ttp_or_ioc == 3:
        ttps = find_TTP(response.iter_lines())
        iocs = find_IoC(response.iter_lines())
        parser_table[url]=dict(ttps, **iocs)
    else:
        print("Wrong Choice")
        return None
    return parser_table