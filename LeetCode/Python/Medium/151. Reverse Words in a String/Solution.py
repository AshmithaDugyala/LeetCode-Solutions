class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        a=s.split()
        j=len(a)-1
        for i in range(len(a)//2):
            a[i],a[j]=a[j],a[i]
            j-=1
        return ' '.join(a)

            