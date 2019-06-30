# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
# 	def invertTree(self, root: TreeNode) -> TreeNode:
class Solution:
	def invertTree(self, root):
		if not root:
			return None
		tmp = self.invertTree(root.left)
		root.left = self.invertTree(root.right)
		root.right = tmp
		return root

