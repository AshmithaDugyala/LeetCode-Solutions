class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        
        maxx=0
        for i in range(len(accounts)):
            a=0
            for j in range(len(accounts[i])):
                a+=accounts[i][j]
                maxx=max(maxx,a)
        return maxx"""
        a=[]
        for i in range(len(accounts)):
            a.append(sum(accounts[i]))
        return max(a)