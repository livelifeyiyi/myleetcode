# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return abs(self.height(root.right) - self.height(root.left)) <= 1 and self.isBalanced(root.right) and self.isBalanced(root.left)
    def height(self, root):
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right)) 