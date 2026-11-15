class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        for i in s:
            if i in "([{":
                stack.append(i)
            elif (i==")" and stack[-1]=="(") or (i=="]" and stack[-1]=="[") or (i=="}" and stack[-1]=="{") :
                stack.pop()
            else:
                stack.append(i)
        if len(stack)==0:
            return True
        else:
            return False