class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        while len(s)>k:
            l=[]
            i=0
            while i<len(s):
                total=0
                a=s[i:i+k]
                for j in a:
                    total+=int(j)
                l.append(str(total))
                i+=k
            s="".join(l)
        return s
        