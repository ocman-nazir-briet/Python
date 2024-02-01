class Person:
    school= "ucp"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printer(self):
        return f"{self.name} - {self.age}"

    @staticmethod
    def welcome():
        return "Welcome to Person Class"

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school
        print("Chnage School from Person ***")

    @property
    def is_adult(self):
        if self.age > 18:
            return 'Adult'
        else:
            return 'Under Age'


# # from instance
# instance = Person('Usman', 24)
# print(instance.welcome())
# print(instance.printer())
# print(instance.is_adult)
# print(instance.school)
# instance.change_school("LUMS")
# print(instance.school)


# # From Class
# print(Person.school)
# Person.change_school("UCP")
# print(Person.school)
# print(Person.welcome())




# Single Inheritence

class Student(Person):
    def __init__(self, name, age, roll):
        Person.__init__(self, name, age)
        self.roll = roll

    def printer(self):
        return f"{self.name} - {self.age} - {self.roll}"
    
    @property
    def is_adult(self):
        if self.age > 18:
            return "Adult"
        else:
            return "Under Age"
        
    
    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school
        print("Chnage School from Student---")

        


# from Instance
instance = Student('Usman nazir', 24, 314)
print(instance.name)
print(instance.printer())
print(instance.welcome())
super(Student, instance).change_school('abc')
instance.change_school('misali')
print(instance.is_adult)

print(Person.printer(instance))

# From Class
print(Person.welcome())
print(instance.school)