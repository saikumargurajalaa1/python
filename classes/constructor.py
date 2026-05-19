# default constructor
# class constclass():
#     def __init__(self):
#         print("default constructor")
# x=constclass()

# parameterized constructor

# class constclass():
#     def __init__(self,a,b):
#         print("i am from constructor")
#         print("value of a is ",a,b)
# x=constclass(10,9)
# y=constclass(20,30)
#

# constructor global var

# class const():
#     gv=30
#     def __init__(self,a,b):
#         self.a=a
#         self.b=8
#     def display(self):
#         self.a=20
#         num=50
#         self.a=num
#         print("im from display method",self.a)
# x=const(10,20)
# print(x.gv)
# x.display()
# print(x.a)

# calling function in constructor

class aa():
    name = "sai"
    def __init__(self):
        print("aa cls am from init",self.name)
        self.menubar()
        self.toolbar()
    def menubar(self):
        print("menubar")
    def toolbar(self):
        print("toolbar")
    def saves(self):
        print("saves")
obj=aa()
obj.saves()

