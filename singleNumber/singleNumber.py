# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:

class Solution:
	def singleNumber(self, nums):
		res = 0
		for num in nums:
			res ^= num
		return res

print(Solution().singleNumber([2,2,1]))
print(Solution().singleNumber([4,1,2,1,2]))
