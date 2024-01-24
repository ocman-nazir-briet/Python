class Parent:
    age = 90
    def __init__(self, name):
        self.name = name
        
    def printer(self):
        return f"This is Parent, {self.name}"

class Child(Parent):
    age = 60
    def __init__(self, name):
        self.name = name
    def printer(self):
        return f"This is Child, {self.name}"
        
class Grandson(Child):
    age = 25
    def __init__(self, name):
        self.name = name
        
    def printer(self):
        return f"This is Grandson, {self.name}"

instance = Grandson("Usman")
print(instance.printer())
print(Child.printer(instance))
print(Child.age)