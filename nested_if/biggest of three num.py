a=int(input("enter a number"))
b=int(input("enter b number"))
c=int(input("enter c number"))

if a==b:
    print(a,b," are bigger")
    if b==c:
        print(b,c,"c are bigger")
elif c==a:
        print(a,c," are bigger")
elif a>b and a>c:
    print(a," is bigger")
elif b>c and b>c:
    print(b," is bigger")
else:
    print(c," is bigger")
