class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def backtrack(subset, i):
            if i == len(s):
                res.append(subset[:])
                return

            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    subset.append(s[i:j+1])
                    backtrack(subset, j + 1)
                    subset.pop()


        backtrack([], 0)
        return res

    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True