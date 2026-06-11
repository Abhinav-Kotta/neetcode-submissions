class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(subset, openP, closeP):
            if openP == closeP == n:
                res.append("".join(subset[:]))

            if openP < n:
                subset.append("(")
                backtrack(subset, openP + 1, closeP)
                subset.pop()
            if closeP < openP:
                subset.append(")")
                backtrack(subset, openP, closeP + 1)
                subset.pop()


        backtrack([], 0, 0)
        return res