class Solution:
	def findRotateSteps(self, ring, key):
		length = len(key)

		for k in key:
			for f, val in enumerate(ring):
				if k == val:
					break
			for b, val in enumerate(ring[::-1]):
				if k == val:
					break
			b += 1
			print("-------------------%s-----------------"%k)
			print("current %s"%(ring))
			if f > b:
				ring = ring[-b:] + ring[0 : -b]
				print("back[%d] is better"%b)
			else:
				ring = ring[f :] + ring[0 : f]
				print("front[%d] is better"%f)
			length += min(f, b)
			print("current %s"%(ring))
		return length


# print(Solution().findRotateSteps("ababcab", "acbaacba"))
print(Solution().findRotateSteps("nyngl","yyynnnnnnlllggg"))
