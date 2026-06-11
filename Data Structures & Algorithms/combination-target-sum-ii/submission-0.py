class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(subset, sum, idx):
            if sum == target:
                res.append(subset[:])

            if sum > target:
                return

            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                subset.append(candidates[i])
                backtrack(subset, sum + candidates[i], i + 1)
                subset.pop()

        backtrack([], 0, 0)
        return res