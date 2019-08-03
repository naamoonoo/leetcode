# class Solution:
# 	def defangIPaddr(self, address: str) -> str:

class Solution:
	def defangIPaddr(self, address):
		return "[.]".join(address.split("."))
		# it's much faster
		# return address.replace(".", "[.]")

print(Solution().defangIPaddr("1.1.1.1"))
