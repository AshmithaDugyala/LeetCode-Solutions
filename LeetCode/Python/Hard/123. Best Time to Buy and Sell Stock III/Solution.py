class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        a=prices[0]
        b=0
        c=[]
        d=0
        for i in prices:
            if i>a:
                b=i-a
                c.append(b)
                a=i
            else:
                a=i

        for i in range(len(c)-1):
            if c[i]<c[i+1] or c[i]==c[i+1]:
                d+=c[i+1]
            if c[i]==c[i-1]:
                return sum(c)
            if c.count(i)==1:
                return c[i]
        return d
