#guess the number game
luckydrawnum=44
noofguess = 1
while(noofguess<=5):
    userinput = int(input("type any num, you have 5 chances"))
    if userinput > luckydrawnum:
        print("your input is greater than the luckydraw number please select a smaller num")
    elif userinput < luckydrawnum:
        print("your input is smaller than the luckydraw number please select a greater num")
    else:
        print("you won!!")
    noofguess=noofguess+1
    if noofguess > 5:
        print("you lose!!")



