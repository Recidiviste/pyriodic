import os
import sqlite3

def connect_table(database):
    conn = None
    try:
        conn = sqlite3.connect(database)
    except Error as e:
        print(e)
    return conn

def table_request(eltype):
    db = connect_table("elements.db")

def general_menu():
    os.system('clear')
    print(30 * "-" , "Sort by", 30 * "-")
    print("1. Name")
    print("2. Number")
    print("3. Symbol")
    print(69 * "-")
    choice('gen', None)

def choice(choice, lenght):
    if choice == 'gen':
        sorting = input("Enter your choice [1-3]: ")
        os.system('clear')
        if sorting == '1':
            el_table('name')
        elif sorting == '2':
                el_table('number')
        elif sorting == '3':
                el_table('symbol')
        else:
            print("Wrong option selection")
            exit()
    elif choice == 'element':
        the_chosen_one = input("Enter your choice [1-{0}]: ".format(lenght))
        print_element(the_chosen_one)

def el_table(sorting):
    i = 0
    db = connect_table("elements.db")
    cursor = db.cursor()
    if sorting=='name':
        cursor.execute('''SELECT name FROM elements''')
        print(18 * "-" , "Names", 18 * "-")
        for nam in cursor.fetchall():
            i += 1
            print(i, ". ", ''.join(nam), sep='')
        print(43 * "-")
        choice('element', i)
    elif sorting=='number':
        cursor.execute('''SELECT number FROM elements''')
        print(17 * "-" , "Numbers", 17 * "-")
        for num in cursor.fetchall():
            i += 1
            print(i, ". ", ''.join(tuple(str(x) for x in num)), sep='')
        print(43 * "-")
        choice('element', i)
    elif sorting=='symbol':
        cursor.execute('''SELECT symbol FROM elements''')
        print(17 * "-" , "Symbols", 17 * "-")
        for sym in cursor.fetchall():
            i += 1
            print(i, ". ", ''.join(sym), sep='')
        print(43 * "-")
        choice('element', i)


def print_element(the_chosen_one):
    element = get_info(the_chosen_one)
    print(element)


general_menu()
