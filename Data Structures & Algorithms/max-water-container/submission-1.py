class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        bigArea = min(heights[l], heights[r]) * (r - l)

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            bigArea = max(area, bigArea)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return bigArea
