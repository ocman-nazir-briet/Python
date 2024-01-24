class Person:
    school = "ucp"
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks
        
    @staticmethod
    def welcome():
        return "Welcome to First Class"
        
    def printer(self):
        return f"{self.name} with roll no {self.roll} got {self.marks} marks."
        
    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school
        
    @property
    def is_pass(self):
        if self.marks >= 33:
            return True
        else:
            return False
            
            
# From Instance
instance = Person("usman", 314, 85)
print(instance.welcome())
print(instance.printer())
print(instance.is_pass)
print(instance.school)
instance.change_school("lums")
print(instance.school)

# From Class
print("Class Data *********************")
print(Person.school)
Person.change_school("ucp")
print(Person.school)
print(Person.welcome())
print("--------------For Single Inheritence----------------")


# For Single Inheritence
class Student(Person):
    def __init__(self, name, roll, marks, grade):
        super().__init__(name, roll, marks)
        self.grade = grade
        
    def printer(self):
        return f"{self.name} - {self.roll} - {self.marks} - {self.grade}"
    
    
inst = Student("usman nazir", 314, 86, 'A')
print(inst.printer())
print(inst.school)
    
print("---------------For Multi Level Inheritence-----------------")
# For Multi Level Inheritence
class Topper(Student):
    def __init__(self, name, roll, marks, grade, position):
        super().__init__(name, roll, marks, grade)
        self.position = position
        
    def printer(self):
        return f"{self.name} got {self.position}."
        
insta = Topper("usman nazir", 314, 86, 'A', "First")
print(insta.printer())
print(insta.school)

# Accessing from class names
print("---------------Accessing from Class Names-----------------")
print(Person.printer(insta))
print(Student.printer(insta))
print(Topper.printer(insta))

# Multiple Inheritence
class Passed(Topper, Student):
    def __init__(self, name, roll, marks, grade, position, passed):
        Topper.__init__(self, name, roll, marks, grade, position)
        Student.__init__(self, name, roll, marks, grade)
        self.passed = passed
        
    def printer(self):
        return f"{self.passed}"
        
instanc = Passed("usman nazir", 314, 86, 'A', "First", "yes")
print(instanc.printer())
