# class Solution:
#     def sortedSquares(self, A: List[int]) -> List[int]:

# sort vs sorted
# array.sort(key..., reversed=...)
# change original array

# sorted(array, key..., reversed...)
# return sorted array, not change origin value

class Solution:
	def sortedSquares(self, A):
		# res = [x ** 2 for x in A]
		# res.sort()
		# return res

		return sorted([x ** 2 for x in A])

print(Solution().sortedSquares([-4,-1,0,3,10]))
print(Solution().sortedSquares([-7,-3,2,3,11]))
