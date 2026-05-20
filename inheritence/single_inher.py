class a():
    def apple(self):
        print("A1")
    def orange(self):
        print("A2")
class b(a):
    def banana(self ):
        print("B1")
x=b()
x.apple()
x.orange()
x.banana()