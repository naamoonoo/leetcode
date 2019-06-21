# class Solution:
# 	def heightChecker(self, heights: List[int]) -> int:

class Solution:
	def heightChecker(self, heights):
		# srt = sorted(heights)
		print(heights - sorted(heights))
		# cnt = 0
		return len(heights - sorted(heights))
		# for i in range(len(heights)):
			# if heights[i] != srt[i]:
			# 	cnt += 1
		# return cnt

print(Solution().heightChecker([1,1,4,2,1,3]))
