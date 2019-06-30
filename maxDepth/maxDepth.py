# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
# 	def maxDepth(self, root: TreeNode) -> int:


class Solution:
	def maxDepth(self, root):
		if not root:
			return 0
		left = self.maxDepth(root.left)
		right = self.maxDepth(root.right)
		if left > right:
			return left + 1
		return right + 1
