class Solution:
	def uniqueMorseRepresentations(self, words):
		alphas = [".-","-...","-.-.","-..",".","..-.","--.","....","..",
		".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
		"..-","...-",".--","-..-","-.--","--.."]
		res = set()
		for word in words:
			tmp = ""
			for c in word:
				tmp += alphas[ord(c) - 97]
			res.add(tmp)
		return len(list(res))

# prettier answer MORSE =
# [".-","-...","-.-.","-..",".","..-.","--.",
#                  "....","..",".---","-.-",".-..","--","-.",
#                  "---",".--.","--.-",".-.","...","-","..-",
#                  "...-",".--","-..-","-.--","--.."]

#         seen = {"".join(MORSE[ord(c) - ord('a')] for c in
#                 word) for word in words}

#         return len(seen)

# join with for expression is used well
print(Solution().uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
