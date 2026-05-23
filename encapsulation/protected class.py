class Bank:
    def __init__(self,username,bankname):
        self.username=username
        self._bankname=bankname
x=Bank("sai","union")
print(x.username)
print(x._bankname)
x.username="kumar"
x.bankname="ICICI"
print(x.username)
print(x._bankname)
