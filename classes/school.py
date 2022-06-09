from classes.staff import Staff
from classes.student import Student

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.objects()
        self.students = Student.objects()

    def list_students(self):
        print('\n')
        for i, student in enumerate(self.students):
            print(f'{i + 1}. {student.name} {student.school_id}')

    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.school_id == student_id:
                return student

    def add_student(self, name, age, new_student_id, password):
        
        new_student = Student(name, age, "Student", new_student_id, password)
        self.students.append(new_student)

    def remove_student(self, old_student_id):
        
        # Loops through each student object and looks for a matching student id
        for i in range(0, len(self.students)):
            if self.students[i].school_id == old_student_id:
                print(f" Is {self.find_student_by_id(old_student_id).name}, {self.find_student_by_id(old_student_id).school_id} who you would like to delete?")
                confirm = input("Yes or No: ")
                if confirm == "Yes":
                    self.students.pop(self.students.index(self.students[i]))
                break # This stops the loop after removing the student, prevents list index out of range error

    
       
        

        

