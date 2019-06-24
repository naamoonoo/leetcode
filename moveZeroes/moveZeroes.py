# class Solution:
# 	def moveZeroes(self, nums: List[int]) -> None:

class Solution:
	def moveZeroes(self, nums):
		nums.sort(key=lambda x: x == 0)
		print(nums)


Solution().moveZeroes([0,1,0,3,12])
