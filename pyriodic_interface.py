import os
import sys
from pyriodic_data import *

def mhelp():
    print("Help :\n- help, h : display this message\n- choose, ch : choose the way to search an element\n- clear: clear the screen\n- exit, quit, q : quit pyriodic\n")

def chelp():
    print("Help :\n- help, h : display this message\n- number, num : display using atomic number\n- name, na : search using name of element\n- symbol, sym : search using symbol\n- clear : clear the screen\n- main, back, b : go back to the main menu\n- quit, q : quit pyriodic\n")

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
        choice = input("\033[92m──\033[94mmain\033[92m──\033[32m>\033[0m ")
        do = choices.get(choice, "Invalid command")
        if do == "Invalid command":
            print(do)
        else:
            exec(do)

def choosing_interface():
    choices = {
            "h": 'chelp()',
            "help": 'chelp()',
            "number": 'print_info("atomicNumber", param)',
            "num": 'print_info("atomicNumber", param)',
            "name": 'print_info("atomicName", param)',
            "na": 'print_info("atomicName", param)',
            "symbol": 'print_info("atomicSymbol", param)',
            "sym": 'print_info("atomicSymbol", param)',
            "clear": 'os.system("clear")',
            "main": 'break',
            "back": 'break',
            "b": 'break',
            "quit": 'sys.exit(0)',
            "q": 'sys.exit(0)'
            }
    while True:
        choice = input("\033[92m──\033[94mchoose\033[92m──\033[32m>\033[0m ")
        command = choice.split(' ')[0]
        if len(choice.split(' ')) == 2:
            param = choice.split(' ')[1]
        do = choices.get(command, "Invalid command")
        if do == "Invalid command":
            print(do)
        elif do == 'break':
            break
        else:
            exec(do)

if __name__ == '__main__':
    main_interface()
