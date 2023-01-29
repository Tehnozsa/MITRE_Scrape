from parsers.Web_Parser import web_parser_menu
from parsers.File_Parser import file_parser_menu
from parsers.Dir_Parser import dir_parser_menu
from parsers.Text_Parser import text_parser_menu
from output.Output import json_output, text_output, file_output, csv_output
from tools.util_func import clearConsole, error


def outputmenu(result):
    functions = [exit, json_output, text_output, file_output, csv_output]
    choice = False
    listChoices = [str(i) for i in range(len(functions))]
    while choice not in listChoices:
        clearConsole()
        
        print("1. JSON Output")
        print("2. Text Output")
        print("3. File Output")
        print("4. CSV Output")
        print("0. Exit")

        choice = input("\nChoose your parser: ")
        choice = choice.strip()
    returnValue = functions[int(choice)](result)
    if returnValue is not True:
        error(returnValue[0],returnValue[1])
    return True


""" Menu options of the program """
def menu():
    functions = [exit, web_parser_menu, file_parser_menu, dir_parser_menu, text_parser_menu]
    choice = False
    listChoices = [str(i) for i in range(len(functions))]
    while choice not in listChoices:
        clearConsole()
        
        print("1. Parse URL")
        print("2. Parse File")
        print("3. Parse Directory")
        print("4. Parse Text")
        print("0. Exit")

        choice = input("\nChoose your parser: ")
        choice = choice.strip()
    returnValue,error_bool = functions[int(choice)]()
    if error_bool is not True:
        error(returnValue[0],returnValue[1])
        return True
    input("The raw result is:\n"+str(returnValue))
    outputmenu(returnValue) 
    return True

def main():
    menuResponse = True
    while menuResponse:
        menuResponse = menu()

if __name__ == '__main__':
	main()