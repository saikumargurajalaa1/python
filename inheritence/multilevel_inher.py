class A():
    def sai(self):
        print("hi")
    def kumar(self):
        print("world")
class B(A):
    def cat(self):
        print("bye")
    def dog(self):
        print("cat")
class C(B):
    def son(self):
        print("come")
x=C()
x.sai()
x.kumar()
x.cat()
x.dog()
x.son