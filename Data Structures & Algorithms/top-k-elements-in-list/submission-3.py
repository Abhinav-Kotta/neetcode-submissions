from heapq import heappush, heappop, heapify
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashmap for counts
        # list of counts as indices and values as the nums
        # go backwards in the list and count k elements into res

        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        freq = [[] for i in range(len(nums) + 1)]
        for num, count in count.items():
            freq[count].append(num)

        res = []
        print(freq)
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                if len(res) < k:
                    print(len(res), k)
                    res.append(j)
                else:
                    return res

        return res