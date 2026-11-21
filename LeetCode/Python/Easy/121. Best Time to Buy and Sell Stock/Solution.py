class Solution(object):
    def maxProfit(self, prices):
     
        maxx=0
        a=prices[0]
        for i in prices[1:]:
            if i>a:
                profit=i-a
                maxx=max(maxx,profit)
            else:
                a=i
        return maxx



























        profit = 0
        buy=prices[0]
        for i in prices[1:]:
            if i>buy:
                profit=max(profit,i-buy)
            else:
                buy=i
        return profit     