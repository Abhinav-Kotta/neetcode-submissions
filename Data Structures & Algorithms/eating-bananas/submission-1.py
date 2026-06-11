class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # max eating k is max of piles array
        # min eating speed is between 1 and max k
        # do binary search on this range to find the smallest k to be under h hours

        l, r = 1, max(piles)
        min_k = r

        while l <= r:
            mid = l + (r - l) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / mid)

            if hours > h:
                l = mid + 1
            else:
                min_k = min(mid, min_k)
                r = mid - 1
            
        return min_k