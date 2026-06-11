import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heapify the array
        # if the array is less than k, then return the first element
        # else pop the first k elements

        pq = []
        for num in nums:
            heapq.heappush(pq, -num)

        res = 0
        
        if len(nums) < k:
            return -nums[-1]
        else:
            for _ in range(k):
                res = heapq.heappop(pq)

        return -res