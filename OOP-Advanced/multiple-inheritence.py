# self belongs the instance/object created
# cls belongs the class and used to acess class variables 

class Person:
    nationality = 'Pakistani'                   # class attribute, it can even be accesed without creating class obj by Person.nationality
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printer(self):
        return f"{self.name} - {self.age}"

    def name_printer(self):
        return f"{self.name} from Person"

    @classmethod
    def change_nationality(cls, new_nationality):
        cls.nationality = new_nationality

    @property
    def is_adult(self):
        if self.age >= 18:
            return True
        else:
            return False
        
    @staticmethod
    def welcome():
        print("Welcome to the Person Class")
    
class Address:
    country = "Pakistan"
    def __init__(self, city):
        self.city = city

    def address_printer(self):
        return self.city

    def name_printer(self):
        return f"{self.name} from Address"

    @classmethod
    def change_country(cls, new_country):
        cls.country = new_country

    
    @staticmethod
    def welcome():
        print("Welcome to the Address Class")

class Student(Person, Address):
    def __init__(self, name, age, city, marks):
        Person.__init__(self, name, age)
        Address.__init__(self, city)
        self.marks = marks

    def name_printer(self):
        return f"{self.name} from Student"

    def marks_printer(self):
        return self.marks

    @staticmethod
    def welcome():
        return "Welcome to the Student Class"


student = Student("Usman Nazir", 24, "Lahore", 99)
print(student.welcome())
print(student.marks_printer())
print(student.name_printer())
print(Person.name_printer(student))         # Function Over Riding (accesing over rided function)
print(Address.name_printer(student))        # Function Over Riding (accessing over rided function)
student.change_nationality("UAE")
student.change_country("UAE")
print(student.name)
print(student.country)
print(student.nationality)
print("****************************")
print(student.name, student.age, student.city, student.marks, student.country)


