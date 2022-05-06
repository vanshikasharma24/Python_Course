l=10
def function(n):
    print(n,"hi")
    # l=5
    # m=8
    global l
    l=l+5
    print(l)#no error
    # print(m)
function("vanshika")
print(l)
#print(m)-->error because its a local scope variable hmara paisa
#global keyword is used to change the global variable
#nested fun
def vanshi():
    x=20
    def atharva():
        global x
        x=50
        print(x)

vanshi()