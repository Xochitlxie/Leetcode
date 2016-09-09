class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timestamp = 1  
        self.user_data = {}
        
    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        if userId not in self.user_data:         
        # Each userId has a tweets list (10 items at most) and a set of followees (include itself)
        self.user_data[userId] = collections.deque(), {userId} 
    
        # Discard outdated tweet    
        if len(self.user_data[userId][0]) == 10:
            self.user_data[userId][0].pop()
        
        self.user_data[userId][0].appendleft((-self.timestamp, tweetId))
        self.timestamp += 1


    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        if userId not in self.user_data:
            return []
        
        heap = []
        for uid in self.user_data[userId][1]:
            if uid in self.user_data:
                for tweet in self.user_data[uid][0]:
                    heapq.heappush(heap, tweet)
                
        res = []
        while len(res) < 10 and heap:
            res.append(heapq.heappop(heap)[1])
        return res

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId not in self.user_data:
            self.user_data[followerId] = collections.deque(), {followerId} 
        
        self.user_data[followerId][1].add(followeeId)


    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId not in self.user_data:
            return
    
        if followerId != followeeId:
            self.user_data[followerId][1].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)