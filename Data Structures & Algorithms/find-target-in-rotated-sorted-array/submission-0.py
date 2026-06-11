class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        # [4,5,6,7,8,9,1,2,3], target = 2
        while l <= r:
            mid = l + (r - l) // 2
            if target == nums[mid]:
                return mid
            
            if nums[mid] >= nums[l]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1

            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1