import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        if len(stones) == 0:
            return 0

        pq = []
        for stone in stones:
            heapq.heappush(pq, -stone)

        while len(pq) > 1:
            first, second = -heapq.heappop(pq), -heapq.heappop(pq)
            if first != second:
                heapq.heappush(pq, -abs(first - second))

        if len(pq) == 1:
            return -pq[0]
        else:
            return 0




        