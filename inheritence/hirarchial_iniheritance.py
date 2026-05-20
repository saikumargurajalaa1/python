class C():
    def sai(self):
        print("sai")
class A(C):
    def kumar(self):
        print("kumar")
class B(C):
    def kumar1(self):
        print("hi")
z=A()
y=B()
z.sai()
z.kumar()
y.sai()
y.kumar1()
