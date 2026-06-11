class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)

        heap = [-cnt for cnt in counts.values()]
        heapq.heapify(heap)
        cooldown = deque()

        time = 0
        while heap or cooldown:
            time += 1
            
            if heap:
                count = heapq.heappop(heap)
                count += 1

                if count < 0:
                    cooldown.append((time + n, count))

            if cooldown and cooldown[0][0] == time:
                _, count = cooldown.popleft()
                heapq.heappush(heap, count)

        return time

            



