import os
import sys
from pyriodic_data import *

def mhelp():
    print("Help :\n- help, h : display this message\n- choose, ch : choose the way to search an element\n- clear: clear the screen\n- exit, quit, q : quit pyriodic\n")

def main_interface():
    os.system('clear')
    print("\nWelcome to Pyriodic !\nType 'help' for information on how to use pyriodic")
    choices = {
            "h": 'mhelp()',
            "help": 'mhelp()',
            "choose": 'choosing_interface()',
            "ch": 'choosing_interface()',
            "clear": 'os.system("clear")',
            "exit": 'sys.exit(0)',
            "quit": 'sys.exit(0)',
            "q": 'sys.exit(0)'
            }
    while True:
        choice = input("\033[91m~\033[92m>\033[0m ")
        do = choices.get(choice, "Invalid command")
        if do == "Invalid command":
            print(do)
        else:
            exec(do)

def choosing_interface():
    choices = {
            "h": 'chelp()',
            "help": 'chelp()',
            "number": 'get_info("atomicNumber", param)',
            "name": 'get_info("atomicName", param)',
            "symbol": 'get_info("atomicSymbol", param)',
            }
    choice = input("\033[91m~\033[92m>\033[0m ")
    command = choice.split(' ')[0]
    param = choice.split(' ')[1]
    do = choices.get(command, "Invalid command")
    if do == "Invalid command":
        print(do)
    else:
        r = exec(do)
        if r == "dtype error":
            print("ERROR")
        else:
            h = Element(r)


if __name__ == '__main__':
    main_interface()
