class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Plan
        # initialize l, r
        # loop through and compare each character
            # make sure each one is alpha numeric
            # if not equal or not alpha numeric, return false

        # return True

        s = s.replace(" ", "")
        l, r = 0, len(s) - 1

        while l < r:
            if l < r and not self.isAlphaNum(s[l]):
                l += 1
            if r > l and not self.isAlphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True

    def isAlphaNum(self, c):
        return ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9')