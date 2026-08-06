import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        rev = ""
        cleared_s= re.sub(r'[^a-zA-Z0-9]', '', s)
        upper_s = cleared_s.upper()
        for ch in upper_s:
            rev = ch + rev
        if rev == upper_s:
            return True
        else:
            return False
