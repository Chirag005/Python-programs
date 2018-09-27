class student:
    def __init__(self,n,a):
        self.full_name=n 
        self.age=a 
    def get_age(self):
        return self.age
    def get_name(self):
        return self.full_name
class Cs_student(student):
    def __init__(self,n,a,s):
        student.__init__(self, n, a)
        self.section_num=self
    def get_age(self):
        print("age:",self.age)
st1=Cs_student("aaa",19,"A")
st1.get_age()
st2=student("vvce",17)
print("name:",st1.get_name())    