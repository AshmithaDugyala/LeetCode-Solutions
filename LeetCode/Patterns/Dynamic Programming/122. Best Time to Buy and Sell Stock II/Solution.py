class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        a=prices[0]
        b=0
        for i in prices:
            if i>a:
                b+=i-a
                a=i
            else:
                a=i
        return b