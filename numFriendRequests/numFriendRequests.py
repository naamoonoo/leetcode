# class Solution:
# 	def numFriendRequests(self, ages: List[int]) -> int:

# class Solution:
# 	def numFriendRequests(self, ages):
# 		counter = 0
# 		for a in range(len(ages)):
# 			for b in range(len(ages)):
# 				if (a != b and ages[b] <= ages[a] and
# 				ages[b] > 0.5 * ages[a] + 7 and not (ages[b] > 100 and ages[a] < 100)):
# 					print("age[%d]:%d -> age[%d]:%d"% (a, ages[a], b, ages[b]))
# 					counter += 1
# 		return counter
# print(Solution().numFriendRequests([16, 16]))
# print(Solution().numFriendRequests([16, 17, 18]))
# print(Solution().numFriendRequests([20,30,100,110,120]))

# in this case, I don't handle duplicate ages.
# if there are 30 people who is 40 years old, will be friend with 20 people, with 20 age and so on...
# so for optimization, I need to make dictionary or array counter for counting duplicated ages
# then by using that ages, can count the friends

# after optimization
class FixedSolution:
	def numFriendRequests(self, ages):
		age_d = {}
		for age in ages:
			if age in age_d:
				age_d[age] += 1
			else:
				age_d[age] = 1
		counter = 0
		for a, a_val in age_d.items():
			for b, b_val in age_d.items():
				if (b <= a and
				b > 0.5 * a + 7 and not (b > 100 and a < 100)):
					counter += a_val * b_val
					if a == b:
						counter -= a_val
		return counter

# c = Solution()
print(FixedSolution().numFriendRequests([16, 16]))
print(FixedSolution().numFriendRequests([16, 17, 18]))
print(FixedSolution().numFriendRequests([20,30,100,110,120]))


