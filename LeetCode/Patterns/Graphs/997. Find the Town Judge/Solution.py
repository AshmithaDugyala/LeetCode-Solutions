class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        count=[0]*(n+1)
        for i in trust:
            count[i[0]]-=1
            count[i[1]]+=1
        for i in range(1,n+1):
            if count[i]==n-1:
                return i
        return -1