import psycopg2


def create_db():
    conn = psycopg2.connect(database="courseTest",
           user="postgres",
           password="89320",
           host="localhost",
           port="5432")
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE courses (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL);''')
    conn.commit()

    cursor.execute('''
    CREATE TABLE students (
        id SERIAL PRIMARY KEY,
        courses_id INTEGER REFERENCES courses (id),
        name VARCHAR(100) NOT NULL,
        gpa NUMERIC(10, 2));''')
    conn.commit()



    cursor.execute("INSERT INTO courses (name) VALUES ('Math');")
    cursor.execute("INSERT INTO courses (name) VALUES ('IT')")
    print('Created tables')
    conn.commit()


    cursor.close()
    conn.close()


def get_students():
    conn = psycopg2.connect(database="courseTest",
           user="postgres",
           password="89320",
           host="localhost",
           port="5432")
    cursor = conn.cursor()
    cursor.execute('SELECT courses.name, students.name FROM courses, students WHERE students.courses_id = courses.id')
    print("All students:")
    for i in cursor.fetchall():
        print(i)

    cursor.close()
    conn.close()



def add_student(student):
        conn = psycopg2.connect(database="courseTest",
                                user="postgres",
                                password="89320",
                                host="localhost",
                                port="5432")
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO students (courses_id, name, gpa) VALUES (%s, %s, %s)", (student['courses_id'], student['name'], student['gpa']))
        conn.commit()

        #cursor.execute("SELECT id FROM students WHERE name=%s", (student["name"],))
        ##id = cursor.fetchone()
        #cursor.execute("INSERT INTO students_courses VALUES (%s, %s);",(student['courses_id']), id)




        cursor.close()
        conn.close()
        print('Successfully added a student')



def get_student(student_id):
    conn = psycopg2.connect(database="courseTest",
                            user="postgres",
                            password="89320",
                            host="localhost",
                            port="5432")
    cursor = conn.cursor()
    cursor.execute("SELECT id, courses_id, name, gpa FROM students WHERE id=%s;", (student_id,))
    print("Student with id", student_id, "is:")
    print(cursor.fetchone())
    cursor.close()
    conn.close()


# Test launch

create_db()

student1 = {'courses_id': 1, 'name': 'Alex M', 'gpa': 4.35}
student2 = {'courses_id': 1, 'name': 'Mary J', 'gpa': 4.36}
student3 = {'courses_id': 2, 'name': 'John S', 'gpa': 4.34}
add_student(student1)
add_student(student2)
add_student(student3)


get_students() # Show all students and courses

get_student(1) # Find a student by id
