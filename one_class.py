class Student:
    def __init__(self, name, student_number, his_class):
        self.name = name
        self.student_number = student_number
        self.his_class = his_class

    def __str__(self):
        return f"{self.name} his id is {self.student_number}, his class is {self.his_class}"


def get_student():
    name = input("Enter student name: ")
    student_number = input("Enter student numb: ")
    class_numb = input("Enter student class number: ")

    student1 = Student(name, student_number, class_numb)

    return student1

print(get_student())