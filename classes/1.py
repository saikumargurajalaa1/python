# class school:
#     a=10
#     def class1(self,a):
#         c=20
#         print("class1",a)
#     def class2(self,b):
#         self.class1(3)
#         print(self.a)
# x=school()
# x.class1(4)
# x.class2(5)

class aa():
    name="ram"
    val=10
    def add(self,x,y):
        num=20
        print("add(param)=",x+y)
        print("add(param+global)=",x+y+self.val)
        print("add(param+global+local)=",x+y+self.val+num)
obj=aa()
obj.add(5,6)
