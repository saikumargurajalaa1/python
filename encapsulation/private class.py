class Bank:
    def __init__(self,username,bankname,balance):
        self.username=username
        self._bankname=bankname
        self.__balance=balance
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self,value):
        self.__balance=value+self.__balance
    @balance.setter
    def withdraw(self,value):
        self.__balance=self.balance-value
x=Bank("alice","union",2000)
print(x.username)
print(x._bankname)
print(x.balance)


x.username="sai"
x._bankname="hdfc"
x.balance=100
print(x.username)
print(x._bankname)
print(x.balance)

x.withdraw=150
print(x.withdraw)

