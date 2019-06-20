# class Solution:
# 	def selfDividingNumbers(self, left: int, right: int) -> List[int]:

class Solution:
	def is_divisable(self, num):
		if '0' in str(num):
			return False
		for i in str(num):
			if num % int(i) != 0:
				return False
		return True

	def selfDividingNumbers(self, left, right):
		res = []
		for num in range(left, right + 1):
			if num % 10 != 0 and self.is_divisable(num):
				res.append(num)
		return res

print(Solution().selfDividingNumbers(66, 708))

