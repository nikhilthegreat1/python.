#self attribute

#class
class Employee:
    name = "harry" #this is class attribute
    language = "python"
    salary = 100000

    def getinfo(self): #in class and object if we make function then we have to use self attribute.
        print(f"the langauge is {self.language}. the salary is {self.salary} ")

    @staticmethod 
    def greet():
        print("good morning")

#object
harry = Employee()
harry.language = "delhi" #this is instance/object attribute
harry.greet()
harry.getinfo()