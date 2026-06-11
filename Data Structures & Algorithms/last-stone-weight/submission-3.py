class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for weight in stones:
            heap.append(-weight)

        heapq.heapify(heap)
        while len(heap) > 1:
            rock1, rock2 = heapq.heappop(heap), heapq.heappop(heap)
            rock1 *= -1
            rock2 *= -1
            diff = abs(rock1 - rock2)
            if diff != 0:
                heap.append(-diff)

        return -heap[0] if len(heap) > 0 else 0
