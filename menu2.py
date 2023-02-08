"""
Program created by Matt Boyer. Group 2 Carter Klimek, Zacharia Salad, Matt Boyer 02/07/2023
"""
"""
A menu - you need to add the database and fill in the functions. 
"""
# Import sqlite
import sqlite3
# Comment added
# Global variable for context manager
db = 'juggling_db.sqlite'
# Main Function
    #Connection to database
def main():
    # Context Manager
    with sqlite3.connect(db) as conn:
        # Call to create_database function
        create_database()
        menu_text = '''
        1. Display all records
        2. Search by name
        3. Add new record
        4. Edit existing record
        5. Delete record 
        6. Quit
        '''
# Function calls by choice
        while True:
            print(menu_text)
            choice = input('Enter your choice: ')
            if choice == '1':
                display_all_records()
            elif choice == '2':
                search_by_name()
            elif choice == '3':
                add_new_record()
            elif choice == '4':
                edit_existing_record()
            elif choice == '5':
                delete_record()
            elif choice == '6':
                break
            else:
                print('Not a valid selection, please try again')


def create_database():
    # Variable created for connection to DB
    with sqlite3.connect(db) as conn:

        conn.execute('DROP TABLE IF EXISTS records')
        # Sets up table
        conn.execute('''
            CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            country TEXT,
            catches INTEGER)      
        ''')
# Test data
        conn.execute('INSERT INTO records(name, country, catches) VALUES (?, ?, ?)', ('Janne Mustonen', 'Finland', 98))
        conn.execute('INSERT INTO records(name, country, catches) VALUES (?, ?, ?)', ('ian Stewart', 'Canada', 94))
        conn.execute('INSERT INTO records(name, country, catches) VALUES (?, ?, ?)', ('Aaron Gregg', 'Canada', 88))
        conn.execute('INSERT INTO records(name, country, catches) VALUES (?, ?, ?)', ('Chad Taylor', 'USA', 78))

        

def display_all_records():
    conn = sqlite3.connect(db)
    records = conn.execute('SELECT * FROM records')
     
# Loops records and displays
    for record in records:
        print(record)
    conn.close()

def search_by_name():
    conn = sqlite3.connect(db)
    search_name = input('Enter name: ')
    conn.execute('SELECT * FROM  records WHERE name=?', (search_name, ))
    records = conn.fetchall()

    for record in records:
        print(record)

def add_new_record():
    # User inputs
    add_name = input('Enter name: ')
    add_country = input('Enter country: ')
    add_catches = int(input('Enter number of catches: '))
    with sqlite3.connect(db) as conn:
        conn.execute(f'INSERT INTO records (name, country, catches) VALUES (?, ?, ?)', (add_name, add_country, add_catches))
    conn.close()
    
    

def edit_existing_record():
# Edit
    update_name = input('Enter name of record holder to edit: ')
    update_new_catches = int(input('Enter new number of catches: '))
    with sqlite3.connect(db) as conn:
        conn.execute('UPDATE records SET catches=? WHERE name=?', (update_new_catches, update_name))

    conn.close()
    

def delete_record():
    
    delete_name = input('Enter name to delete: ')
    with sqlite3.connect(db) as conn:
        conn.execute('DELETE FROM records WHERE name=?', (delete_name, ))
    conn.commit()

if __name__ == '__main__':
    main()