from classes.school import School 

school = School('Ridgemont High') 

while True:
    mode = input("\nWhat would you like to do?\nOptions:\n1. List All Students\n2. View Individual Student <student_id>\n3. Add a Student\n4. Remove a Student <student_id>\n5. Quit\n")

    if mode == '1':
        school.list_students()
    elif mode == '2':
        student_id = input('Enter student id:')
        student_string = str(school.find_student_by_id(student_id))
        print(student_string)
    elif mode == "3":
        name = input("Please input the student's name: ")
        age = input("Please input the student's age: ")
        role = "Student"
        new_student_id = input("Please input the student's ID: ")
        password = input("Please give the student a unique password: ")
        school.add_student(name, age, role, password, new_student_id)
    elif mode == "4":
        find_student_id = input("Enter the student's unique ID: ")
        school.remove_student(find_student_id)
    elif mode == '5':
        break


# Working through discrepancy of creating a new student class/instance vs instructions (dictionary)

# print(school.list_students)
# school.students.append({"name": "Dalton"})
# print(school.students)
# print(school.students[0].name)
# print(school.students[6]["name"]) # print(school.students[6].name) doesn't work

