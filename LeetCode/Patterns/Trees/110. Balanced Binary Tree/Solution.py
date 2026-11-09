# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        if root is None:
            return True
        def height(root):
            if root is None:
                return 0
            a = height(root.left)
            b = height(root.right)
            if abs(a-b) > 1:
                return -1
            if a == -1 or b == -1:
                return -1
            return max(a,b) + 1
        return height(root) != -1