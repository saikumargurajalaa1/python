num1=float(input("enter a number"))
num2=float(input("enter a number"))
op=input("enter operator + - * /:")
if op=="+":
    print(num1+num2)
elif op=="-":
    print(num1-num2)
elif op=="*":
    print(num1*num2)
elif op=="/":
    print(num1/num2)
else:
    print("invalid choice")