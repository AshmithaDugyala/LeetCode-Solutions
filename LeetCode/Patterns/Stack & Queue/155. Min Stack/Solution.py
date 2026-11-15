class MinStack(object):

    def __init__(self):
        self.s1=[]
        self.s2=[]
    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.s1.append(value)
        if len(self.s2)==0 or value<=self.s2[-1]:
            self.s2.append(value)
    def pop(self):
        """
        :rtype: None
        """
        if self.s1[-1]==self.s2[-1]:
            self.s2.pop()
        self.s1.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.s1[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.s2[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()