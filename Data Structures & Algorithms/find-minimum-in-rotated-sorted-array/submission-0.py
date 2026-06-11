class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        curr_min = float('inf')
        while l < r:
            m = l + (r - l) // 2
            curr_min = min(nums[m], curr_min)
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1


        return min(curr_min,nums[l])