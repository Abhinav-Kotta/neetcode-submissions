class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        t_count = Counter(t)
        window = {}

        have, need = 0, len(t_count)
        res, min_length = [-1, -1], float('inf')

        l = 0
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)
            if s[r] in t_count and window[s[r]] == t_count[s[r]]:
                have += 1
                
            while have == need:
                if (r - l + 1) < min_length:
                    res = [l, r]
                    min_length = r - l + 1
                window[s[l]] -= 1
                if s[l] in t_count and window[s[l]] < t_count[s[l]]:
                    have -= 1
                l += 1


        l, r = res
        return s[l:r+1] if min_length != float('inf') else ""
                

