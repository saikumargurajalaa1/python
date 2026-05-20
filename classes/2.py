# without return
# class aa():
#   def add(self,x,y):
#       print(x+y)
#
# x=aa()
# x.add(4,5)

#with return using class
# class aa():
#   def add(self,x,y):
#      return x+y
#
# x=aa()
# print(x.add(4,5))

#position argument using class
# class aa():
#   def add(self,age,name):
#       print("age is",age,"name is",name)
#
# x=aa()
# x.add(23,"sai")

# default argument using class
# class aa():
#   def add(self,age,name="sai",marks=20):
#       print("age is",age,"name is",name,"marks are",marks)
#
# x=aa()
# x.add(23,"kumar",78)
# x.add(24,"sita",89)

#keyword argument
# class aa():
#   def add(self,age,name,marks):
#       print("age is",age,"name is",name,"marks are",marks)
#
# x=aa()
# x.add(name="kumar",age=23,marks=78)

#multiple arguments * args using return

# class sai():
#     def add(self,*args):
#         s=0
#         for i in args:
#             s=s+i
#         return s
# x=sai()
# print(x.add(2,3,4,5,6))

# without return

# class sai():
#     def add(self,*args):
#         s=0
#         for i in args:
#             s=s+i
#         print(s)
# x=sai()
# x.add(2,3,4,5,6)

# calling function in class

class sai():
    def kumar(self):
        print("2")
        self.piano()
        self.nano()
    def nano(self):
        print("3")
    def piano(self):
        print("4")


x=sai()
x.kumar()



