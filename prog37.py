# #one function can be assigned to the other fun and that can run even after deleting one function
# def fun1():
#     print("fun1")
# fun2=fun1
# del fun1
# fun2()
# #a function can return a function
# def funncret(num):
#     if num==1:
#         return print
#     if num==0:
#         return sum
# a=funncret(1)
# print(a)
# #a function can take function as parameter
# def executer(fun):
#     fun("hii")
# executer(print)
# decorator


def dec1(func1):
    def nowexec():
        print("Executing now")
        func1()
        print("Executed")
        return nowexec

@dec1
def who_is_harry():
    print("Harry is a good boy")

who_is_harry = dec1(who_is_harry)

who_is_harry()

