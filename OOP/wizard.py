class Wizard:
    def __init__(self, name, patronus):
        if not name:
            raise ValueError("missing name")
        self.name = name
        

    ...



class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house



    ...


class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    ...




student = Student('harry', 'gryffindor')
proffessor = Professor('severus', "defense against the dark arts")

print(student.name)