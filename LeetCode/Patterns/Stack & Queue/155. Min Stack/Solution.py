class MinStack(object):

    def __init__(self):
        self.s1=[]

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        return self.s1.append(value)

    def pop(self):
        """
        :rtype: None
        """
        return self.s1.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.s1[-1]

    def getMin(self):
        """
        :rtype: int
        """
    
        return minn


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()