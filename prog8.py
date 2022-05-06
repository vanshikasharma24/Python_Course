#if and elif
var1 = 2
var2 = 5
var3 = int(input())
if var3>var2:
    print("greater")
elif var3==var2:
    print("equal")
else:
    print("lesser")

list = [1,2,3,4,5]

if 2 in list:
    print('its there')
if 2 not in list:
    print("not there")