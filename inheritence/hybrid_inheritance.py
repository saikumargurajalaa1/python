class A:
    def sai(self):
        print("sai")
class B(A):
    def kumar(self):
        print("kumar")
class C(A):
    def chow(self):
        print("chow")
class D(B,C):
    def cop(self):
        print("cop")
x=D()
x.sai()
x.kumar()
x.chow()
x.cop()