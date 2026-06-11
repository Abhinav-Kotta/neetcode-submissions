from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # have an output array and a queue
        # have an outer loop to loop through nums
        # once you check every k elements get the left most element in queue and append to output
        # return output

        output, q = [], deque()
        l = r = 0

        for i in range(len(nums)):
            # make sure no smaller values exist in the queue
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1

            r += 1

        return output

            
