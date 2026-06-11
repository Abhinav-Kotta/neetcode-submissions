class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numTodig = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }

        res = []
        def backtrack(subset, i):
            if len(subset) == len(digits):
                res.append("".join(subset[:]))
                return

            for dig in numTodig[digits[i]]:
                subset.append(dig)
                backtrack(subset, i + 1)
                subset.pop()

        if digits:
            backtrack([], 0)
        return res