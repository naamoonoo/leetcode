# class Solution:
#     def repeatedNTimes(self, A: List[int]) -> int:

# O(len(set(A)) * len(A))
# class Solution:
# 	def repeatedNTimes(self, A):
# 		counter = len(A) / 2
# 		for n in set(A):
# 			tmp = list(filter(lambda x : x == n, A))
# 			if len(tmp) == counter:
# 				return n


class Solution:
	def repeatedNTimes(self, A):
		res = {}
		for n in A:
			if n in res:
				res[n] += 1
			else:
				res[n] = 1
		counter = len(A) / 2
		for n in set(A):
			if res[n] == counter:
				return n
print(Solution().repeatedNTimes([1,2,3,3]))
print(Solution().repeatedNTimes([2,1,2,5,3,2]))
print(Solution().repeatedNTimes([5,1,5,2,5,3,5,4]))

# collections.Counter
import collections
class CounterSolution:
	def repeatedNTimes(self, A):
		count = collections.Counter(A)
		print(count)
		for k in count:
			print(k)
			if count[k] > 1:
				return k

# if well understand the question,

class SetSolution:
	def repeatedNTimes(self, A):
		uniq = set()
		for n in A:
			if n not in uniq:
				uniq.add(n)
			else:
				return n



print(CounterSolution().repeatedNTimes([1,2,3,3]))
print(CounterSolution().repeatedNTimes([2,1,2,5,3,2]))
print(CounterSolution().repeatedNTimes([5,1,5,2,5,3,5,4]))
