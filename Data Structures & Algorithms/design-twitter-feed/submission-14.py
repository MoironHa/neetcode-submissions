from datetime import datetime
class Twitter:

    def __init__(self):
        self.tweets = []
        self.follows = defaultdict(set)
        self.timestamp = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        heapq.heappush(self.tweets, (-self.timestamp, userId, tweetId))
        return

        

    def getNewsFeed(self, userId: int) -> List[int]:
        popped = []
        res = []
        while self.tweets and len(res) < 10:
            tweet = heapq.heappop(self.tweets)
            popped.append(tweet)

            time, tweeter, tweetId = tweet

            if tweeter == userId or tweeter in self.follows[userId]:
                res.append(tweetId)
        

        for tweet in popped:
            heapq.heappush(self.tweets, tweet)


        return res        

    def follow(self, followerId: int, followeeId: int) -> None:
        # if followerId not in self.follows:
        #     self.follows[followerId] = set()
        self.follows[followerId].add(followeeId)
        return
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # if followerId in self.follows:
        self.follows[followerId].discard(followeeId)
        return
        
