class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans=""
        strs=sorted(strs)
        f=strs[0]
        l=strs[-1]
        for i in range(min(len(f),len(l))):
            if(f[i]!=l[i]):
                return ans
            ans+=f[i]

        return ans