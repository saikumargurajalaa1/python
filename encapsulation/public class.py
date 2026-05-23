class Bank:
    def __init__(self,username):
        self.username=username
x=Bank("alice")
x.username="bob"
print(x.username)
