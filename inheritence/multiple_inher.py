class A():
    def sai(self):
        print("hello")
class B():
    def kumar(self):
        print("world")
class C(A,B):
    def chow(self):
        print("python")
x=C()
x.sai()
x.kumar()
x.chow()