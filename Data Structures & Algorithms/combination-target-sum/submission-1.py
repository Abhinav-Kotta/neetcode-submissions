class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(subset, sum, idx):
            if sum == target:
                res.append(subset[:])
                return

            for i in range(idx, len(nums)):
                if sum + nums[i] > target:
                    return

                subset.append(nums[i])
                backtrack(subset, sum + nums[i], i)
                subset.pop()
                

                
        backtrack([], 0, 0)
        return res
