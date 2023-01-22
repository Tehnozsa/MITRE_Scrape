from parsers.Web_Parser import web_parser_menu
from parsers.File_Parser import file_parser_menu
from parsers.Dir_Parser import dir_parser_menu
from parsers.Text_Parser import text_parser_menu
from tools.util_func import clearConsole, error

""" Menu options of the program """
def menu():
    functions = [exit, web_parser_menu, file_parser_menu, dir_parser_menu, text_parser_menu]
    choice = False
    listChoices = [str(i) for i in range(len(functions))]
    while choice not in listChoices:
        clearConsole()
        print("MITRE/IoC Parser")
        print("---------------------------------------------------------------------\n")
        
        print("1. Parse URL")
        print("2. Parse File")
        print("3. Parse Directory")
        print("4. Parse Text")
        print("0. Exit")

        choice = input("\nChoose your parser: ")
        choice = choice.strip()
    returnValue = functions[int(choice)]()
    print(returnValue)
    if returnValue is not True:
        error(returnValue[0],returnValue[1])
    return True

def main():
    menuResponse = True
    while menuResponse:
        menuResponse = menu()

if __name__ == '__main__':
	main()