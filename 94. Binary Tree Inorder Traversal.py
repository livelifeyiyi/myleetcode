import binaryTree
class Solution(object):
	def inorderTraversal(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		stack = [root]
		res = []
		while stack:
			node = stack.pop()
			if isinstance(node, int):
				res.append(node)
				continue
			if node:
				if node.right:
					stack.append(node.right)
				stack.append(node.val)
				if node.left:
					stack.append(node.left)
		return res
		'''
		#node = root
		if node:
			res = self.inorderTraversal(node.left)
			res.append(node.val)
			res = self.inorderTraversal(node.right)'''
		return res
data = [1, None, 2, None, None,3]
tree = binaryTree.BinaryTree()
root = tree.initTree(data)
s = Solution()
print s.inorderTraversal(root)
