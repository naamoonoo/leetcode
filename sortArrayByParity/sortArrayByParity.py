# class Solution:
#     def sortArrayByParity(self, A: List[int]) -> List[int]:


class Solution:
	def sortArrayByParity(self, A):
		return list(filter(lambda x: x % 2 == 0, A)) + list(filter(lambda x: x % 2 == 1, A))


print(Solution().sortArrayByParity([3,1,2,4]))


#https://www.programiz.com/python-programming/methods/list/sort

# sort(key=..., reverse=...)
# key would be the function like len(built in function) or personal function
# in this time, key function return 0 or 1, but It is sorting algoritmm
# ######so, smaller number would comes first!#######
# 0 -> even , 1 -> odd

# python built in sort function
# Python uses an algorithm called Timsort:

# Timsort is a hybrid sorting algorithm, derived from merge
# sort and insertion sort, designed to perform well on many
# kinds of real-world data. It was invented by Tim Peters in
# 2002 for use in the Python programming language. The
# algorithm finds subsets of the data that are already
# ordered, and uses the subsets to sort the data more
# efficiently. This is done by merging an identified subset,
# called a run, with existing runs until certain criteria
# are fulfilled. Timsort has been Python's standard sorting
# algorithm since version 2.3. It is now also used to sort
# arrays in Java SE 7, and on the Android platform.

class SortSolution:
	def sortArrayByParity(self, A):
		A.sort(key = lambda x: x % 3)
		return A

print(SortSolution().sortArrayByParity([3, 1, 2, 4, 5, 6]))
