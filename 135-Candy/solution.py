class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        res = [1] * len(ratings)
        for i in range(len(ratings)-1):
            if ratings[i] < ratings[i+1]:
                res[i+1] = res[i] + 1
        print res
        for j in range(-1,-len(ratings),-1):
            if ratings[j] < ratings[j-1]:
                if res[j-1] < res[j] + 1:
                    res[j-1] = res[j] + 1
        print res
        return sum(res)