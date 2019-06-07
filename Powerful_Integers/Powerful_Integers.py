class Solution:
	def powerfulIntegers(self, x, y, bound):
		res = set()
		i = 0
		while x**i <= bound:
			j = 0
			while y**j <= bound:
				if x**i + y**j <= bound:
					res.add(x**i + y**j)
				if y == 1 and j == 0:
					break
				j += 1
			if x == 1 and i == 0:
				break
			i += 1
		return list(res)

c = Solution()
print(c.powerfulIntegers(2, 1, 10))
