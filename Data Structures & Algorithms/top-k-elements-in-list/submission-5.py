class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # find top most k frequent words
        # this is a bucket sort problem
        # make a dictionary that has all the counts
        # make a ferq array of the max number of times a number can be repeated
            # indicies are count and the value is the num
        # loop backwards and append each number to res until length of res is k

        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        freq = [[] for _ in range(len(nums) + 1)]
        print(len(freq))
        for key, value in count.items():
            freq[value].append(key)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                if len(res) < k:
                    print(len(res), k)
                    print(res)
                    res.append(j)
                else:
                    break
        return res