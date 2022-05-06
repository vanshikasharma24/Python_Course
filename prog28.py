#args and kwargs
# def fun(a,b,c,d,e):
#     print(a,b,c,d,e)
# fun(1,2,3,4,5)
# cant update the print statement without updating the fun thats why we use agrs and kwargs
#arg take tuple as a argument and kwargs take dictionary as an argument
#order : normal argumnt , args , kwargs

def myfun(normal,*args,**kwargs):
    print(normal)
    for i in args:
        print(i)
    for key ,items in kwargs.items():
        print(key,items)
normal="hi i am a normal argument"
vanshika=["hii","hello","python","java"]
kwarg={"morining":"sun","night":"moon","food":"kachori","drink":"fanta"}
myfun(normal,*vanshika,**kwarg)




