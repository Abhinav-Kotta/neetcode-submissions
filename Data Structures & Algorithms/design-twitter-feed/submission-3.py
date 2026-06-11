class Twitter:

    def __init__(self):
        self.count = 0
        self.userTweets = defaultdict(list)
        self.followers = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userTweets[userId].append([self.count, tweetId])
        self.count -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        self.followers[userId].add(userId)
        minHeap, res = [], []

        for followeeId in self.followers[userId]:
            if followeeId in self.userTweets:
                index = len(self.userTweets[followeeId]) - 1
                count, tweetId = self.userTweets[followeeId][index]

                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)

            if index >= 0:
                count, tweetId = self.userTweets[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
