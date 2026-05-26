#traditional way of method overloading

# class A:
#     def add(self,a,b):
#         print(a+b)
#     def add(self,a,b,c,d):
#         print(a+b+c+d)
# x=A()
# x.add(1,2)
# x.add(1,2,3,4)

# #using default arguments
#
# class A():
#     def add(self,a,b,c=3,d=4):
#         print(a+b+c+d)
# x=A()
# x.add(1,2)
# x.add(1,2,3,)
# x.add(1,2,3,4)

#using variable length argument(*args)
class A:
    def dispaly(self,*args):
        print(args)
x=A()
x.dispaly(1,2)
x.dispaly(1,2,3,4)
