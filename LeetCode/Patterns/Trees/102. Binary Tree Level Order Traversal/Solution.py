# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        a=[]
        if root is None:
            return a
        queue=[]
        queue.append(root)
        while len(queue)>0:
            temp=[]
            for i in range(len(queue)):
                currnode=queue.pop(0)
                if currnode.left:
                    queue.append(currnode.left)
                if currnode.right:
                    queue.append(currnode.right)
                temp.append(currnode.val)
            a.append(temp)
        return a