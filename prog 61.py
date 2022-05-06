#os module implementation
#OS module provides our code with a direct connection to the operating system.
import os
print(dir(os))
print(os.getcwd())
# os.chdir("c://")
# print(os.getcwd())
print(dir("c://"))
# f=open("sharma")#error because directry changed and program searches in current directry
print(os.listdir("c://"))
# os.makedirs("this/that")
# os.rename("sharma1","sharmajii")
print(os.environ.get('Path'))
print(os.path.join("C:/", "sharma"))
print(os.path.isfile("C://$SysReset"))
