# class Solution:
# 	def numUniqueEmails(self, emails: List[str]) -> int:

class Solution:
	def numUniqueEmails(self, emails):
		res = set()
		for mail in emails:
			local = mail.split('@')[0].split('+')[0].replace('.', '')
			domain = mail.split('@')[1]
			res.add(local + '@' + domain)
		return len(list(res))

# regex solution possible!
print(Solution().numUniqueEmails(['test.email+alex@leetcode.com','test.e.mail+bob.cathy@leetcode.com','testemail+david@lee.tcode.com']))
