# class Solution:
#     def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:


class Solution:
	def invert_img(self, img):
		for i, v in enumerate(img):
			if v == 0:
				img[i] = 1
			elif v == 1:
				img[i] = 0
		return img

	def flipAndInvertImage(self, A):
		res = []
		for a in A:
			a.reverse()
			res.append(self.invert_img(a))
		return res

# map(function, iterable, ...)
# map return -> map object(iterator)
# to use as list, need to make a list like set
#
def flipAndInvertImage(A):
	res = []
	for img in A:
		res.append(list(map(lambda x: 0 if x == 1 else 1, img[::-1])))
	return res


# built in list manipulation method
# def flipAndInvertImage(self, A):
#         """
#         :type A: List[List[int]]
#         :rtype: List[List[int]]
#         """
#         result = []
#         for row in A:
#             result.append(list(map(lambda x: 0 if x == 1 else 1, row[::-1])))
#         return result
print(Solution().flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))
print(Solution().flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))
print(flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))
print(flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))
