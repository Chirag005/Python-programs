class priv:
    def __init__(self,x,y):
        self.__x=x 
        self.y=y 
    def increment(self):
        self.__x=self.__x+1
        self.y=self.y+1
a=priv(5,6)
print(a._priv__x)
a.increment()
print('value of x after increment',a.__x)
print('value of y after increment',a.y)
