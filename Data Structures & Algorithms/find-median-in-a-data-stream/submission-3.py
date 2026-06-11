class MedianFinder:
    # find the median of an array
    # create a nums array to append values to when added
    # in findMedian, if the length of array is odd, return len array // 2
        # if length of array is even, return (len(array) // 2 + len(array) // 2 - 1) // 2
    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)

    def findMedian(self) -> float:
        minHeap = []
        print(self.nums)
        for num in self.nums:
            minHeap.append(num)

        print(minHeap)

        heapq.heapify(minHeap)

        print(minHeap)
        if len(self.nums) % 2 == 0:
            firstIndex = (len(self.nums) // 2) - 1
            secondIndex = firstIndex + 1

            print(f"first index {firstIndex} second Index{secondIndex}")

            i = 0
            elementOne = 0
            while i <= firstIndex:
                elementOne = heapq.heappop(minHeap)
                i += 1

            elementTwo = heapq.heappop(minHeap)
            print(elementOne, elementTwo)
            return (elementOne + elementTwo) / 2
             
        else:
            midIndex = len(self.nums) // 2
            i = 0
            midElement = 0
            while i <= midIndex:
                midElement = heapq.heappop(minHeap)
                i += 1

            return midElement
        