def pal(a):
    if len(a)<1:
        return True
    else:
        if a[0]==a[-1]:
            return pal(a[1:-1])
        else:
            return False
a=str(input("enter the string"))
if pal(a)==True:
    print("palindrome")
else:
    print("not a palindrome")
    
