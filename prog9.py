#faulty calculater
a=int(input("type first num to the calculater"))
b=int(input("type second num to the calculater"))
operator=input("select operator from +,-,/,*")
if operator == ("+"):
    if a==56 and b==9:
        print("77")
    else:
        num1=a+b
        print(num1)
elif operator == ("-"):
    num2=a-b
    print(num2)
elif operator == ("*"):
    if a==45 and b==3:
        print("555")
    else:
        num3=a*b
        print(num3)
elif operator == ("/"):
    if a==56 and b==6:
        print("4")
    else:
        num4=a/b
        print(num4)
else:
    print("error/out of range")