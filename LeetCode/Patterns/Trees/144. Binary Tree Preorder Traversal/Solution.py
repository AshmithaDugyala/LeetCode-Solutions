# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        a=[]
        if root is None:
            return []
        a.append(root.val)
        a+=self.preorderTraversal(root.left)
        a+=self.preorderTraversal(root.right)
        return a