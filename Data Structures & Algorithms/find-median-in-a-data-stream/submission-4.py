class MedianFinder:
    # find the median of an array
    # create a nums array to append values to when added
    # in findMedian, if the length of array is odd, return len array // 2
        # if length of array is even, return (len(array) // 2 + len(array) // 2 - 1) // 2
    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        # check if small <= large
        if self.small and self.large and (-1 * self.small[0] > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # check the lengths are a difference of 1
        if len(self.small) - len(self.large) > 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) - len(self.small) > 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.small) < len(self.large):
            return self.large[0]

        return (self.large[0] + (-1 * self.small[0])) / 2