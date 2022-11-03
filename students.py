import connection


def menu():
    print("""
    1. Insert student
    2. Update student
    3. Delete student
    4. Select student
    5. Select all students
    0. Exit
    """)
    options = int(input("Select an option: "))
    return options


def insert_student():
    first_name = input("Enter the first name: ")
    last_name = input("Enter the last name: ")
    note_1 = int(input("Enter the first note: "))
    note_2 = int(input("Enter the second note: "))
    average = (note_1 + note_2) / 2
    query = "insert into students (first_name, last_name, note_1, note_2, average) values (?, ?, ?, ?, ?)"
    parameters = (first_name, last_name, note_1, note_2, average)
    connection.query_students(query, parameters)
    print("Student inserted successfully")


def update_student():
    student_id = int(input("Enter the student id: "))
    first_name = input("Enter the first name: ")
    last_name = input("Enter the last name: ")
    note_1 = int(input("Enter the first note: "))
    note_2 = int(input("Enter the second note: "))
    average = (note_1 + note_2) / 2
    query = "update students set first_name = ?, last_name = ?, note_1 = ?, note_2 = ?, average = ? where id = ?"
    parameters = (first_name, last_name, note_1, note_2, average, student_id)
    connection.query_students(query, parameters)
    print("Student updated successfully")


def delete_student():
    student_id = int(input("Enter the student id: "))
    query = "delete from students where id = ?"
    parameters = (student_id,)
    connection.query_students(query, parameters)
    print("Student deleted successfully")


def select_student():
    student_id = int(input("Enter the student id: "))
    query = "select * from students where id = ?"
    parameters = (student_id,)
    student = connection.query_students(query, parameters)
    print(f"{'ID':<5}{'First Name':<15}{'Last Name':<15}{'Note 1':<10}{'Note 2':<10}{'Average':<10}")
    for data in student:
        number, first_name, last_name, note_1, note_2, average = data
        print(f"{number:<5}{first_name:<15}{last_name:<15}{note_1:<10}{note_2:<10}{average:<10}")


def all_students():
    query = "select * from students"
    students = connection.query_students(query)
    print(f"{'ID':<5}{'First Name':<15}{'Last Name':<15}{'Note 1':<10}{'Note 2':<10}{'Average':<10}")
    for student in students:
        number, first_name, last_name, note_1, note_2, average = student
        print(f"{number:<5}{first_name:<15}{last_name:<15}{note_1:<10}{note_2:<10}{average:<10}")


if __name__ == "__main__":
    option = menu()
    while option != 0:
        if option == 1:
            insert_student()
        elif option == 2:
            update_student()
        elif option == 3:
            delete_student()
        elif option == 4:
            select_student()
        elif option == 5:
            all_students()
        else:
            print("Invalid option")
        option = menu()

