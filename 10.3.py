#self attribute

#class
class Employee:
    name = "harry" #this is class attribute
    language = "python"
    salary = 100000

    def __init__(self, name, language, salary): #__init__ is dunder method which runs automatically when we create object
        self.name = name
        self.language = language
        self.salary = salary
        print("i am creating an object")

    def getinfo(self): #in class and object if we make function then we have to use self attribute.
        print(f"the langauge is {self.language}. the salary is {self.salary} ")

    @staticmethod 
    def greet():
        print("good morning")

#object
harry = Employee("harry", "python", 100000)
harry.language = "delhi" #this is instance/object attribute
print(harry.language, harry.salary)