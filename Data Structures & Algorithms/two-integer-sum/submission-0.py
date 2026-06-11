class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mappy = {}
        res = []
        for i in range(len(nums)):
            mappy[nums[i]] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in mappy and mappy[diff] != i:
                return [i, mappy[diff]]