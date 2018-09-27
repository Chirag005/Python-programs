empid=1001
basic=15000
allowances=6000
gross=basic+allowances
if gross<5000:
    tax=0
elif gross in range(5001,10001):
    tax=(10/100)*gross
elif gross in range(10001,20001):
    tax=(20/100)*gross
else:
    tax=(30/100)*gross
net=gross-tax
print("employee id=",empid)
print("basic salary=",basic)
print("allowances=",allowances)
print("gross pay=",gross)
print("income tax=",tax)
print("net pay=",net)
