str=input("enter the string")
i=0
a=0
count=0
while i<len(str):
    if str[i].isupper():
        a+=1
        print(str[i])
    i+=1
print(a)
for j in str:
   if str[str.index(j)].isupper():
    count+=1
print(count)
    
    

