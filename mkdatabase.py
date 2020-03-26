from os import path
import sqlite3
import npyscreen

def Tui(*args): # The form to enter new element or modify existing element
    F = npyscreen.Form(name='New/Modify Element') # Name of the form
    NorM = F.add(npyscreen.TitleSelectOne, max_height=3, # Form to know if it's
                 name="What do you want to do ?", # New or Modify
                 values = ['New', 'Modify'], # Element
                 scroll_exit = True # Permit the scroll to exit
                 ) # End of theadding tothe form
    number = F.add(npyscreen.TitleText, name='Number') # Number of the element
    name = F.add(npyscreen.TitleText, name='Name') # Name of the element
    symbol = F.add(npyscreen.TitleText, name='Symbol') # Symbol of the element
    atomic_weight = F.add(npyscreen.TitleText, name='Atomic Weight') # Atomic Weight of the element
    F.edit() # Permit the editing
    return [NorM.value, int(number.value), name.value, symbol.value, float(atomic_weight.value)] # Return a list full of informations


def create_connection(database): # The function to connect the database
    # create a database connection to a SQLite database
    conn = None # connection is None
    try: # Try to connect
        conn = sqlite3.connect(database) # let conn equal be the connection to database
    except Error as e: # If can't connect (non existing DB)
        print(e) # Print error message
    finally: # And 
        if conn: # If conn still exist
            conn.close() # Close the connection


def create_table(database): # Create the table structure
    db = sqlite3.connect(database) # Connect to the DB
    cursor = db.cursor() # Create a cursor to act on DB
    cursor.execute('''
        CREATE TABLE elements(id INT PRIMARY KEY, number INTEGER,
                              name TEXT, symbol TEXT, atomic_weight REAL
                              )
                ''') # Create the base structure (id, number, name, symbol, atomic_weight
    db.close() # Close the connection to the DB


def create_elements(database): # Add the element to the DB
    results = npyscreen.wrapper_basic(Tui) # Get the results with the Form
    db = sqlite3.connect(database) # Connect to the DB
    cursor = db.cursor() # Cursor to act on the DB
    if results[0][0] == 0: # If we choose to add an element
        cursor.execute('''INSERT INTO elements(id, number, name, symbol, atomic_weight)
                          VALUES(?,?,?,?,?)''', (results[1], results[1], results[2], results[3], results[4])) # Create the element with the values
    elif results[0][0] == 1: # IF we choose to edit an element
        cursor.execute('''UPDATE elements SET number = ?, name = ?, symbol = ?, atomic_weight = ? WHERE id = ?''',(results[1], results[2], results[3], results[4], results[1])) # Update the elememebt
    db.commit() # Commit the changes
    db.close() # Close the connection to the DB


def print_elements(database): # Print element from DB
    db = sqlite3.connect(database) # Connect to databse
    cursor = db.cursor() # Create a cursor to act on the DB
    cursor.execute('''SELECT number, name, symbol, atomic_weight FROM elements''') # Retreive all the element
    all_rows = cursor.fetchall() # Put the retreived data on a variable
    for row in all_rows:
        # row[0] returns the first column in the query (name), row[1] returns email column.
        print('Element : {0}\nName : {2}\nSymbol : {1}\nAtomic Weight : {3}\n\n'.format(row[0], row[1], row[2], row[3])) # Print each data with the signification


if __name__ == '__main__': # If the program is executed as main
    db = "elements.db" # the name of the db
    print_elements(db) # Print the current elements of the db
    input("Press Enter to continue...") # Wait for the user to continue
    create_connection(db) # Test if you can connect
    if not path.exists(db): # If te DB don't exist
        create_table(db) # create the table in a DB
    create_elements(db) # Create the elements in the DB
