import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []

        for point in points:
            distance = (point[0] ** 2) + (point[1] ** 2)
            heapq.heappush(pq, [distance, point[0], point[1]])

        res = []
        for _ in range(k):
            dist, x, y = heapq.heappop(pq)
            res.append([x, y])

        return res


        
        
