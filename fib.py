n=int(input("enter the no"))
fib=[0,1]
i=0
while i<n-2:
    fib.append(fib[i]+fib[i+1])
    i+=1
print(fib)

