import psycopg2


def create_db():
    conn = psycopg2.connect(database="librarytest",
           user="postgres",
           password="89320",
           host="localhost",
           port="5432")
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE books (
        id INTEGER PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        author VARCHAR(50));''')
    conn.commit()

    cursor.execute('''
    CREATE TABLE shelves (
        shelf_id SERIAL PRIMARY KEY,
        book_id INTEGER REFERENCES books(id) ON DELETE CASCADE);''')
    conn.commit()



    cursor.execute("INSERT INTO books VALUES (1010, 'Fairytales', 'John Smith');")
    cursor.execute("INSERT INTO books VALUES (1020, 'Roadtrip', 'Ann Maxwell');")
    cursor.execute("INSERT INTO shelves(book_id) VALUES (1010);")
    cursor.execute("INSERT INTO shelves(book_id) VALUES (1020);")
    print('Created tables')
    conn.commit()


    cursor.close()
    conn.close()

def add_book():
    book_id = int(input("Enter book's id: "))
    name = input("Enter book's name:")
    author = input("Enter book's author: ")

    conn = psycopg2.connect(database="librarytest",
           user="postgres",
           password="89320",
           host="localhost",
           port="5432")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO books VALUES (%s, %s, %s);", (book_id, name, author))
    conn.commit()
    cursor.execute("INSERT INTO shelves(book_id) VALUES (%s);", (book_id,))
    conn.commit()

    print("Successfully added a new book")

def delete_book():
    book_id = int(input("Enter id of a book which you want to delete: "))
    conn = psycopg2.connect(database="librarytest",
           user="postgres",
           password="89320",
           host="localhost",
           port="5432")
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM books WHERE id=%s", (book_id,))
        conn.commit()
        print("Successfully deleted a book")

    except Exception:
        print('Most likely book with such id does not exist')

def show_book():
    book_id = int(input("Enter id of a book you want to get: "))

    conn = psycopg2.connect(database="librarytest",
           user="postgres",
           password="89320",
           host="localhost",
           port="5432")
    cursor = conn.cursor()

    cursor.execute('''SELECT books.id, books.name, books.author, shelves.shelf_id AS shelf
FROM books JOIN shelves
ON shelves.book_id = books.id
WHERE books.id=%s;''', (book_id,))

    data = cursor.fetchone()
    if data is not None:
        print(f'''
Book's id is {data[0]}
Book's name is {data[1]}
Book's author is {data[2]}
Book is on shelf {data[3]}
''')


def last_ten_books():
    conn = psycopg2.connect(database="librarytest",
           user="postgres",
           password="89320",
           host="localhost",
           port="5432")
    cursor = conn.cursor()

    cursor.execute('''SELECT books.id, books.name, books.author, shelves.shelf_id AS shelf
    FROM books JOIN shelves
    ON shelves.book_id = books.id
    ORDER BY shelves.shelf_id DESC
    LIMIT 10;''')

    data = cursor.fetchall()
    if data is not None:
        for i in data:
            print(f'''
Book's id {i[0]}, name {i[1]}, author {i[2]}, on shelf {i[3]}
''')


create_db()
while True:
    command = input('''Choose an action:
1 - add a new book
2 - delete a book
3 - show info about a book by an id
4 - show last 10 added books
0 - exit
''')

    if command == '1':
        add_book()
    elif command == '2':
        delete_book()
    elif command == '3':
        show_book()
    elif command == '4':
        last_ten_books()
    elif command == '0':
        break
    else:
        print("Invalid command. Try again")
