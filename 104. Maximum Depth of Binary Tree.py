# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class SolutionBFS(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nodes = [root] if root else []
        depth = 0
        while nodes:
            depth += 1
            nodes = filter(lambda x:x, [i for j in nodes if j for i in [j.left, j.right]])
        return depth
class solutionRecursive(object):
    def maxDepth(self, arg):
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        