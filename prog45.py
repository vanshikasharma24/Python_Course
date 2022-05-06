#aam khao gutli mt gino
#to achieve abstraction we use encapsulation(tohide the implimentation details)
#idea of wrapping data and the methods that work on data within one unit.
#Abstraction refers to hiding unnecessary details to focus on the whole product instead of parts of the project separately.
# Abstraction helps us in partitioning the program into many independent concepts so we may hide the
# irrelevant information in the code.
#multi level inheritance
class Employee:
    var=10
    no_of_leaves=7#class variable
    #"Constructor in Python is used to assign values to the variables or data members of a class when an object is created."
    def __init__(self,astd,asalary,arole):
        self.std=astd
        self.salary=asalary
        self.role=arole
    def printdetails(self):#object
        print(f"the std is {self.std} salary is {self.salary}and the role is {self.role}")

class Player:
    vqr=8
    def __init__(self,aname,agame):
        self.name=aname
        self.game=agame
    def playerdetails(self):
        print(f"the name is {self.name} and the game is {self.game}")

class coolprogrammer(Employee,Player):
    # var=7
    language="c++"
    def printlang(self):
        print(self.language)
harry=coolprogrammer(5,555,"jbj")

# harry.printdetails()
print(harry.var)
