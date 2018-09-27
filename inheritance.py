class a:
    def add(self,x,y):
        return x+y
class b(a):
    def sub(self,x,y):
        return x-y
obj=b()
print(obj.add(5,6))
print(obj.sub(8,4))