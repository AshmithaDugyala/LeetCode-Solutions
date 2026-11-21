class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
    
        great=0
        for i in range(len(accounts)):
            a=0
            for j in range(len(accounts[i])):
                a+=accounts[i][j]
                great=max(great,a)
        return great