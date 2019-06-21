# class Solution:
# 	def diStringMatch(self, S: str) -> List[int]:

class arrSolution:
	def diStringMatch(self, S):
		arr = list(range(len(S) + 1))
		res = []
		for c in S:
			if c == 'I':
				res.append(arr.pop(0))
			elif c == 'D':
				res.append(arr.pop(len(arr) - 1))
		res.append(arr.pop(0))
		return res

class Solution:
	def diStringMatch(self, S):
		lo = 0
		hi = len(S)
		res = []
		for c in S:
			if c == 'I':
				res.append(lo)
				lo += 1
			elif c == 'D':
				res.append(hi)
				hi -= 1
		res.append(lo)
		return res

print(Solution().diStringMatch("IDID"))
print(Solution().diStringMatch("III"))
print(Solution().diStringMatch("DDI"))
