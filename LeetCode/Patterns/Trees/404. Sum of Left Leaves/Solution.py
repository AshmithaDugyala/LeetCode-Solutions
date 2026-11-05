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
            return a
        if root.left is not None:
            if root.left.left is None and root.left.right is None:
                a+=root.left.val
            else:
                a+=self.sumOfLeftLeaves(root.left)
        a+=self.sumOfLeftLeaves(root.right)
        return a