# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        a=[]
        if root is None:
            return []
        a+=self.inorderTraversal(root.left)
        a.append(root.val)
        a+=self.inorderTraversal(root.right)
        return a
        