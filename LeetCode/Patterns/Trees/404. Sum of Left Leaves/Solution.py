# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        a=0
        if root is None:
            return
        if root.left is None and root.right is None:
            return 0
        a=root.left.val+root.right.left.val
        
        return a