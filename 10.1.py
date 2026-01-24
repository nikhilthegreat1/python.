#class
class Employee:
    name = "harry" #this is class attribute
    langauge = "python"
    salary = 100000

#object
harry = Employee()
harry.city = "delhi" #this is instance/object attribute
print(harry.name, harry.langauge, harry.city)