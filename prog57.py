#FOR LOOP WITH ELSE
#When we use else with for loop, the compiler will only go into the else block of code when two conditions are satisfied:

#The loop is normally executed without any error.
#We are trying to find an item that is not present inside the list or data structure on which we are implementing our loop.
# for i in "vanshika":
#     print(i)
# else:
#     print("program ended successfully")

lst=[1,2,3,4,7,8]
for i in lst:
    if i == 10:
        break
else:
    print("element not found")