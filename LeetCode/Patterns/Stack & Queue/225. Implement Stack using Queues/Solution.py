"""class MyStack(object):

    def __init__(self):
        self.s1=[]
        self.s2=[]

    def push(self, x):
       
        self.s1.append(x)

    def pop(self):
       
        if not self.s1 and not self.s2:
            return -1
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()


    def top(self):
       
        if not self.s1 and not self.s2:
            return -1
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop(0))
        return self.s2[1]

    def empty(self):
       
        return len(self.s1) + len(self.s2)==0"""


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
class MyStack(object):

    def __init__(self):
        self.q = []

    def push(self, x):
        self.q.append(x)

        for i in range(len(self.q)-1):
            self.q.append(self.q.pop(0))

    def pop(self):
        return self.q.pop(0)

    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q) == 0