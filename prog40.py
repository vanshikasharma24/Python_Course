#methods and constructor
class Employee:
    no_of_leaves=7#class variable
    #Constructor in Python is used to assign values to the variables or data members of a class when an object is created."
    def __init__(self,astd,asalary,arole):
        self.std=astd
        self.salary=asalary
        self.role=arole
    def printdetails(self):#object
        print(f"the std is {self.std} salary is {self.salary}and the role is {self.role}")

#class variable cant be changed by object it can be changed by class only
#class variable is shared by all the instances4d

harry=Employee(9,455,"instructor")
rohan=Employee(9,4555,"student")
harry.printdetails()
rohan.printdetails()
# harry.std=9#instance variable
# harry.salary=455
# harry.role="instructor"
# rohan.std=9
# rohan.salary=4555
# rohan.role="student"
# rohan.printdetails()