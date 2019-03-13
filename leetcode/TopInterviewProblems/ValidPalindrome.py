import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        table = str.maketrans(dict.fromkeys(string.punctuation))
        s = list(s.lower().replace(" ", "").translate(table))
        return s == s[::-1]