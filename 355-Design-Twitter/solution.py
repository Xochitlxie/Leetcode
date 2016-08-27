class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.follow = {}
        self.message = {}
        
    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        if userId not in self.follow.keys():
            self.follow[userId] = set([userId])
        for user in list(self.follow[userId]):
            if user not in self.message.keys():
                self.message[user] = []
            self.message[user].append((tweetId,userId))
        
    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        result = []
        while len(result) < 10 and not self.message[userId]:
            messageId, uId = self.message[userId].pop()
            if uId in self.follow[userId]:
                result.append(messageId)
        return list(self.message[userId])

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followeeId not in self.follow.keys():
            self.follow[followeeId] = set([followeeId])
        self.follow[followeeId].add(followerId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId in self.follow[followeeId]:
            self.follow[followeeId].remove(followerId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)