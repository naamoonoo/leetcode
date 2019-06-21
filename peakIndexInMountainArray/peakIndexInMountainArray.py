# class Solution:
# def peakIndexInMountainArray(self, A: List[int]) -> int:

class Solution:
	def peakIndexInMountainArray(self, A):
		for i, a in enumerate(A):
			if A[i - 1] < a and a > A[i + 1]:
				break
		return i

print(Solution().peakIndexInMountainArray([0,1,0]))
print(Solution().peakIndexInMountainArray([0,2,1,0]))
