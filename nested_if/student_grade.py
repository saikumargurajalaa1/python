tel=int(input("telugu"))
hin=int(input("hindi"))
eng=int(input("english"))
math=int(input("math"))
sci=int(input("science"))

total=tel+hin+eng+math+sci
avg=total/5

print("total=",total)
print("avg=",avg)

if(tel>=35 and hin>=35 and eng>35 and math>=35 and sci>=35):
    if(avg>=75 and avg<=100):
        print("first class")
    elif(avg>=60 and avg<75):
        print("second class")
    elif(avg>=35 and avg<60):
        print("third class")
else:
    print("fail")
