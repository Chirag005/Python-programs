stack=[]
size=10
def is_empty(stack):
    if stack==[]:
        return True
    else:
        return False
def is_full(stack):
    if len(stack)>=size:
        return True
    else:
        return False
def display(stack):
    i=len(stack)-1
    while i>-1:
        print(stack[i],"\n")
        i-=1
def push(a,stack):
    if is_full(stack)==True:
        print("stack is full")
        return
    else:
        stack.append(a)
        display(stack)
def pop(stack):
    if is_empty(stack)==True:
        print("stack underflow")
        return
    else:
        item=stack.pop()
        print(item)
        display(stack)
while (1):
    choice=int(input("\nMENU\n1.PUSH\n2.POP\n"))
    if choice==1:
        a=int(input("enter the no to be pushed"))
        push(a,stack)
    elif choice==2:
        pop(stack)
    else:
        print("invalid choice")
        break
        
       

             
             


    

