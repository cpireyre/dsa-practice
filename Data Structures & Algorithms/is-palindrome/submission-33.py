import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        xs = set(string.ascii_letters + string.digits)
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and s[l] not in xs: l += 1
            while l < r and s[r] not in xs: r -= 1
            if s[l].lower() != s[r].lower(): return False
            l += 1; r -= 1
        return True