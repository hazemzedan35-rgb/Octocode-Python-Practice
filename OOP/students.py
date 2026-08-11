class Student: 
    def __init__(self, name, house):
        if not name:
            raise ValueError("missing name.")
        self.name = name
        self.house = house
        
    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name not in ["Harry", "Hermione"]:
            raise ValueError("invalid name")
        self._name = name


    @property 
    def house(self):
        return self._house
  
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("invalid house")
        self._house = house
    

def main():  
    student = get_student()
    print(student)
   
 
def get_student():
    name = input("Name: ")
    house = input("House: ").title()   
    student = Student(name, house)
    return student


if __name__=="__main__":
    main()

 
       