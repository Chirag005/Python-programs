import timeit
start=timeit.default_timer()
class student:
    def __init__(self,name,usn):
        self.name=name
        self.usn=usn
    def display(self):
        print("name=",self.name)
        print("usn=",self.usn)
s1=student('chaithra','4vv16cs023')
s2=student('adithi','4vv16cs044')
s1.display()
s2.display()
stop=timeit.default_timer()
print(stop-start)       