class Bankaccount:
    def __init__(self,accountnumber,name,reg,bal):
        self.accountnumber=accountnumber
        self.name=name
        self.reg=reg
        self.bal=bal

    def checkbal(self):
        print(self.bal)

    def withdraw(self,money):
        pass

    def  deposit(self,money):
        pass

    def transfer(self, payee, amount):
        self.bal-=amount
        payee.bal+=amount
        print("$"+str(amount)+" has been transferred from"+self.name+" to "+payee.name)

var1=Bankaccount("1234","firstnamelastname","111111111",1000)
var2=Bankaccount("1235","notme","111111112",69)

var1.checkbal()
var2.checkbal()
var1.deposit(100)
var1.transfer(var2,200)