class Solution:
    def findMin(self, nums: List[int]) -> int:
        # establish regular l and r

        l, r = 0, len(nums) - 1
        min_element = float('inf')


        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        return nums[l]
