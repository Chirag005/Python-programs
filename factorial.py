# factorial funtion calling itself recursively
def factorial(number):
    if number==0:
        return 1
    else:
        return number*factorial(number-1)
#calling factorial function
raw_input=input("enter the number to compute factorial:")
number = int(raw_input)
result=factorial(number)
print("the factorial of",number,"is",result)
