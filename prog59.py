#finally and else with try and except
f1=open("vanshika")
try:
    f=open("unknown.txt")
except Exception as e:
    print("bde bde shehro me esi chhoti chhoti bate hoti rehti he senurita")
    print(e)
#you can except different exception by different except statements
else:
    print("it will only run if exception is not running")
finally:
    f1.close()
    print("finally code")
