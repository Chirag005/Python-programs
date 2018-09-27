import timeit
start=timeit.default_timer()
class bank_acc:
    def __init__(self,name,acc_num,bal):
        self.name=name
        self.acc_num=acc_num
        self.bal=bal
    def withdrawal(self):
        amt=int(input("enter the amount to be withdrawn"))
        self.bal=self.bal-amt
        self.display()
    def deposit(self):
        amt=int(input("enter the amount to be deposited"))
        self.bal=self.bal+amt
        self.display() 
    def display(self):
        print("name=",self.name)
        print("acc_num",self.acc_num)
        print("bal=",self.bal)
n1=bank_acc('aaa','2659298',20000)
n2=bank_acc('bbb','2655665',30000)
n3=bank_acc('ccc','5628919',40000)
print(n1.name)
n1.deposit()
n1.withdrawal()
n2.deposit()
n2.withdrawal()
n3.deposit()
n3.withdrawal()
stop=timeit.default_timer()
print(stop-start)       

        
