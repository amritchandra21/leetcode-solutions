class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        rWords = s.split()
        rWords = rWords[::-1]
        return " ".join(rWords)
