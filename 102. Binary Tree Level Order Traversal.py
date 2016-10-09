# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res,next = [],[]
        if root:
            tmp = [root]
        else: return res
        res.append(tmp)
        while 1:
            for i in tmp:
                if i.left:
                    next.append(i.left)
                if i.right:
                    next.append(i.right)
            if next == []: break
            res.append(next)
            tmp = list(next)
            next = []
        return [[x.val for x in i] for i in res]
            
class Solution2(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        nodes, vals = [root] if root else [], []
        while nodes:
            vals.append(map(lambda x:x.val, nodes))
            nodes = filter(lambda x: x, [i for j in nodes if j for i in [j.left, j.right]])
        return vals
class InvertedOrder(object):
    def levelOrderBottom(self, root):
        nodes, vals = [root] if root else [], []
        while nodes:
            vals.insert(0,map(lambda x:x.val, nodes))
            nodes = filter(lambda x: x, [i for j in nodes if j for i in [j.left, j.right]])
        return vals          