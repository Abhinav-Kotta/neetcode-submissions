class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = min(heights[l], heights[r]) * (r - l)

        while l < r:
            total_area = min(heights[l], heights[r]) * (r - l)
            max_area = max(max_area, total_area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_area