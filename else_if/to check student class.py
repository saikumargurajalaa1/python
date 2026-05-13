tel=int(input("enter the marks"))
hin=int(input("enter the marks"))
eng=int(input("enter the marks"))
math=int(input("enter the marks"))
sci=int(input("enter the marks"))
total=tel+hin+eng+math+sci
avg=total/5
print("total is",total)
print("average is",avg)

if avg>=75 and avg<=100:
    print("first class")
elif avg>=60 and avg<75:
    print("second class")
elif avg>=35 and avg<60:
    print("third class")
else:
    print("fail")