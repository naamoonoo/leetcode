# class Solution:
#     def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:


class Solution:
	def getSmall(self, a, b):
		if a > b:
			return b
		return a


	def maxIncreaseKeepingSkyline(self, grid):
		v = []
		h = []

		nums = len(grid)
		for y in range(nums):
			tmp = grid[y][0]
			for x in range(nums):
				if grid[y][x] > tmp:
					tmp = grid[y][x]
			h.append(tmp)
		# print(h)
		for x in range(nums):
			tmp = grid[0][x]
			for y in range(nums):
				if grid[y][x] > tmp:
					tmp = grid[y][x]
			v.append(tmp)
		# print(v)
		res = 0
		for y in range(nums):
			for x in range(nums):
				# print(grid[y][x])
				if grid[y][x] < self.getSmall(v[x], h[y]): ## -> min
					# print("vertical %d, horizintal %d, value %d" %
						# (v[x], h[y], grid[y][x]))
					res += self.getSmall(v[x], h[y]) - grid[y][x]
		# print(res)
		return res

class BetterSolution():
	def maxIncreaseKeepingSkyline(self, grid):
		max_row = [max(row) for row in grid]
		max_col = [max(col) for col in zip(*grid)]

		return sum(min(max_row[r], max_col[c]) - val
			for r, row in enumerate(grid)
			for c, val in enumerate(row)
		)

# [1, 2, 3], [a, b, c] => (zip) => [1, a], [2, b], [3, c]
# [1, a], [2, b], [3, c] => (unzip) => [1, 2, 3], [a, b, c]

# The * operator can be used in conjuncton with zip() to unzip the list.

# zip(*zippedList)
# Example 3: Unzipping the Value Using zip()
# script.py
# IPython Shell
# 
# coordinate=['x''y''z']
# value=[34509]
# result=zip(coordinatevalue)
# resultList=list(result)
# print(resultList)
# cv=zip(*resultList)
# print('c ='c)
# print('v ='v)
# Run
# Session Inactive
# Powered by DataCamp
# When you run the program, the output will be:

# [('x', 3), ('y', 4), ('z', 5)]
# c = ('x', 'y', 'z')
# v = (3, 4, 5)
print(Solution().maxIncreaseKeepingSkyline([
	[3, 0, 8, 4],
	[2, 4, 5, 7],
	[9, 2, 6, 3],
	[0, 3, 1, 0]
]))

print(BetterSolution().maxIncreaseKeepingSkyline([
	[3, 0, 8, 4],
	[2, 4, 5, 7],
	[9, 2, 6, 3],
	[0, 3, 1, 0]
]))

