# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
##TLE
class Solution1(object):
	def findPath(self, root, target):
		if root:
			return int(root.val == target) + self.findPath(root.left, target-root.val) + self.findPath(root.right, target- root.val)
		return 0
	def pathSum(self, root, sum):
		"""
		:type root: TreeNode
		:type sum: int
		:rtype: int
		"""
		if root:
			return self.findPath(root,sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
		return 0

class Solution(object):
	def pathSum(self, root, sum):
		self.count = 0
		preDict = {0:1}
		def dfs(p, target, pathSum, preDict):
			if p:
				pathSum += p.val
				self.count += preDict.get(pathSum - target, 0)
				preDict[pathSum] = preDict.get(pathSum, 0) + 1
				print preDict
				dfs(p.left, target, pathSum, preDict)
				dfs(p.right, target, pathSum, preDict)
				preDict[pathSum] -= 1
		dfs(root, sum, 0, preDict)
		return self.count

import binaryTree
data = [10,5,-3,3,2,2,11,3,-2,2,1]
tree = binaryTree.BinaryTree()
root = tree.initTree(data)
S =Solution()
print S.pathSum(root, 8)