class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(subset):
            if len(subset) == len(nums):
                res.append(subset[:])
            
            for num in nums:
                if num not in subset:
                    subset.append(num)
                    backtrack(subset)
                    subset.pop()

        backtrack([])
        return res