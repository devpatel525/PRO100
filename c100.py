class Atm(object):
    def __init__(self,cashWithdraw,balanceinqury,cardnumber):
        self.cashWithdraw=cashWithdraw
        self.balanceinqury=balanceinqury
        self.cardnumber=cardnumber
        
    def receive(self):
        print("start")

    def deposited(self):
        print("stopped")


Atm("withdrawed","totalmoney","123456788999898")
print(Atm.withdrawed()) 
print(Atm.deposited())