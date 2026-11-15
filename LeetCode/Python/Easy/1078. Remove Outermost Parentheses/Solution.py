class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        """
        stack=[]
        count=0
        for i in s:
            if i==")":
                count-=1
            if count>0:
                stack.append(i)
            if i=="(":
                count+=1
    
        return "".join(stack)"""

        res=""
        c=0
        for i in s:
            if i=="(":
                if c>0:
                    res+=i
                c+=1
            else:
                c-=1
                if c>0:
                    res+=i
        return res