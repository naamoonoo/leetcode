# class Solution:
#     def judgeCircle(self, moves: str) -> bool:


class Solution:
	def judgeCircle(self, moves):
		# location = [0, 0]
		# for cmd in moves:
		# 	if (cmd == "U"):
		# 		location[1] += 1
		# 	elif (cmd == "D"):
		# 		location[1] -= 1
		# 	elif (cmd == "R"):
		# 		location[0] += 1
		# 	elif (cmd == "L"):
		# 		location[0] -= 1
		# return location[0] == 0 and location[1] == 0

		x = y = 0
		for cmd in moves:
			if cmd == "U" : y += 1
			elif cmd == "D" : y -= 1
			elif cmd == "R" : x += 1
			elif cmd == "L" : x -= 1
		return x == y == 0

print(Solution().judgeCircle("UD"))
print(Solution().judgeCircle("LL"))


# counting method
# by using collections.Counter()
from collections import Counter
class CounterSolution:
	def judgeCircle(self, moves):
		# cnt = Counter(moves)
		# return cnt["R"] - cnt["L"] == cnt["U"] - cnt["D"] == 0

# built in count method - fastest one!!
		return moves.count("R") - moves.count("L") == moves.count("U") - moves.count("D") == 0


print(CounterSolution().judgeCircle("UD"))
print(CounterSolution().judgeCircle("LL"))

