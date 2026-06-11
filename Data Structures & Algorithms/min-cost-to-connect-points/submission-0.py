class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {i:[] for i in range(N)}

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                cost = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([cost, j])
                adj[j].append([cost, i])

        totalCost = 0
        visited = set()
        minHeap = [[0, 0]]
        while len(visited) < N:
            cost, i = heapq.heappop(minHeap)
            if i in visited:
                continue
            totalCost += cost
            visited.add(i)
            for cost, neighbor in adj[i]:
                if neighbor not in visited:
                    heapq.heappush(minHeap, [cost, neighbor])

        return totalCost
    