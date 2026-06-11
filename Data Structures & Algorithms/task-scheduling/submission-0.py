import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # make a q and a max heap
        # after you process element in max heap, append it to queue with new count and the updated time it can be proccessed
        countTasks = Counter(tasks)
        pq = []
        for k, v in countTasks.items():
            heapq.heappush(pq, -v)

        print(pq)
        q = deque()
        time = 0
        while q or pq:
            time += 1

            if not pq:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(pq)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(pq, q.popleft()[0])
        return time