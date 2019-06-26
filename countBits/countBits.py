# class Solution:
# 	def countBits(self, num: int) -> List[int]:


class Solution:
	def getBits(self, n):
		cnt = 0
		while n != 0:
			if n & 1:
				cnt += 1
			n = n >> 1
		return cnt

	def countBits(self, num):
		res = []
		for n in range(num + 1):
			res.append(self.getBits(n))
		return res

print(Solution().countBits(2))
print(Solution().countBits(5))
