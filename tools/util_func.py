""" Function that prints the program logo """
import os
import sys

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