class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) < k:
            return []

        distances = []
        for point in points:
            dist = math.sqrt((point[0] ** 2) + (point[1] ** 2))
            distances.append((dist, point))

        heapq.heapify(distances)
        res = []

        for _ in range(k):
            res.append(heapq.heappop(distances)[1])

        return res
