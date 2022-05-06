#aam khao gutli mt gino
#to achieve abstraction we use encapsulation(tohide the implimentation details)
# idea of wrapping data and the methods that work on data within one unit.
#Abstraction refers to hiding unnecessary details to focus on the whole product instead of parts of the project separately.
# Abstraction helps us in partitioning the program into many independent concepts so we may hide the
# irrelevant information in the code.
#inheritance
#methods and constructor
class Employee:
    no_of_leaves=7#class variable
    #"Constructor in Python is used to assign values to the variables or data members of a class when an object is created."
    def __init__(self,astd,asalary,arole):
        self.std=astd
        self.salary=asalary
        self.role=arole
    def printdetails(self):#object
        print(f"the std is {self.std} salary is {self.salary}and the role is {self.role}")

#class variable cant be changed by object it can be changed by class only
#class variable is shared by all the instances
class Programmer(Employee):
    no_of_holiday=45
    def __init__(self,astd,asalary,arole,alang):
        self.std = astd
        self.salary = asalary
        self.role = arole
        self.lang= alang


    def printprog(self):
        print(f"the std is {self.std} salary is {self.salary}and the role is {self.role}and the no of language are{self.lang}")

# harry=Employee(9,455,"instructor",["java"])
harry=Programmer(9,455,"instructor")
harry.printdetails()
# rohan=Employee(9,4555,"student",["c++"])
atharva=Programmer(7,600,"PROGRAMMER",["PYTHON"])
atharva.printprog()
harry.printprog()
harry.printdetails()
rohan.printdetails()
