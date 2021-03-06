# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        return self.equ(root.left, root.right)
        
    def equ(self,p,q):
        if p == None and q == None:
            return True
        if (p == None and q != None) or (p != None and q == None):
            return False
        return p.val == q.val and self.equ(p.left,q.right) and self.equ(p.right, q.left)