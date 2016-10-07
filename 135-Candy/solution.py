class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if len(ratings) <= 1:
            return len(ratings)
        countDown,prev,total = 0,1,1
        for i in range(1,len(ratings)):
            if ratings[i] >= ratings[i-1]:
                if countDown > 0 :
                    total += countDown*(countDown+1)/2
                    if countDown >= prev:
                        total += countDown - prev + 1
                    countDown = 0
                    prev = 1
                if ratings[i] == ratings[i-1]:
                    prev = 1
                else:
                    prev += 1
                total += prev
            else:
                countDown += 1
        if countDown > 0:
            total += countDown*(countDown+1)/2  
            if countDown >= prev:
                total += countDown - prev + 1
        return total