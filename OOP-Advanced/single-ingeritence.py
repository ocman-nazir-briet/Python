# self belongs the instance/object created
# cls belongs the class and used to acess class variables 

class Person:
    nationality = 'Pakistani'                   # class attribute, it can even be accesed without creating class obj by Person.nationality
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printer(self):
        return f"{self.name} - {self.age}"
    
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
        print("Welcome to the Python")
    
# For Instance
person_instance = Person("Usman", 24)
person_instance.welcome()
print(person_instance.printer())
print("Before Change: ", person_instance.nationality)
person_instance.change_nationality("UAE")
print("After Change: ", person_instance.nationality)
print("Is Adult: ", person_instance.is_adult)

# For class
print('\n')
Person.welcome()
print("After Change: ", Person.nationality)         # Accessing from Person class instead of Instance/Obj
Person.change_nationality("Saudi")
print("After Change: ", Person.nationality)
print("Instance After 2nd Change: ", person_instance.nationality)
