class stack(object):
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return self.items==[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
s1=stack()
s1.push(1)
s1.push(2)
s1.push('one')
s1.push('two')
print(s1.is_empty())
print(s1.peek())
    
    