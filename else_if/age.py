a=int(input("enter your age"))

if a<18:
    print("child")
elif a>18 and a<=25:
    print("teen")
elif a>25 and a<60:
    print("adult")
else:
    print("senior")