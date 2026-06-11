class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        # len 5
        # k = 3

        kthLargest = 0
        for i in range(len(nums) - k + 1):
            kthLargest = heapq.heappop(nums)

        return kthLargest