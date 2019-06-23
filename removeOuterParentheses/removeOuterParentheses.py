	# class Solution:
	# def removeOuterParentheses(self, S: str) -> str:

class Solution:
	def removeOuterParentheses(self, S):
		res = ""
		is_opened = 0
		for c in S:
			if c == '(':
				is_opened += 1
				if is_opened != 1:
					res += c
			elif c== ')':
				is_opened -= 1
				if is_opened != 0:
					res += c
		return res

print(Solution().removeOuterParentheses("(()())(())"))
print(Solution().removeOuterParentheses("(()())(())(()(()))"))
print(Solution().removeOuterParentheses("()()"))


