class Twitter:
    # Whole Idea:
    # we maintain a heap, and for each following by that user, it is in there
    # So if user follows 3 people, there are 3 nodes in heap
    # 


    def __init__(self):
        # Need dict for tweets, following and time
        self.tweetMap = defaultdict(list) # give user -> list of [time, tweetID]
        self.followingMap = defaultdict(set) # give user -> set of [userId]
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        # POST tweet.
        # To post a tweet, we append to the list of the user
        self.time -= 1
        self.tweetMap[userId].append([self.time, tweetId])


        

    def getNewsFeed(self, userId: int) -> List[int]:
        # Idea: build a heap with the last post of each followee. 
        res = []
        minHeap = []
        # Follow yourself
        self.followingMap[userId].add(userId)
        # for each person you follow
        for followeeId in self.followingMap[userId]:
            if followeeId in self.tweetMap: # if the following has any post
                index = len(self.tweetMap[followeeId]) - 1 # Index of last post
                time, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [time, tweetId, followeeId, index-1])
        while minHeap and len(res) < 10:
            # if minHeap still has post and we don't have 10 post yet
            time, tweetId, followeeId, index = heapq.heappop(minHeap)
            # tweetId: append to res
            res.append(tweetId)
            # followeeId: add back to heap if still have things
            if index >= 0:
                time, tweetId = self.tweetMap[followeeId][index] 
                heapq.heappush(minHeap, [time, tweetId, followeeId, index-1])
        return res
                
                
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followingMap[followerId].add(followeeId) # add followeeId in set


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followingMap[followerId]: # if followeeId is in set
            self.followingMap[followerId].remove(followeeId)
        
