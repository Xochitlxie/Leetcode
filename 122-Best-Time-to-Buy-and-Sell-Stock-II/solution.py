class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        if len(prices) < 2:
            return result
        curMin = prices[0]
        lastPrice = prices[0]
        for i in range(1,len(prices)):
            if prices[i] >= lastPrice:
                lastPrice = prices[i]
                curMin = min(curMin,prices[i])
            else:
                result += lastPrice - curMin
                curMin = prices[i]
                lastPrice = prices[i]
        result += lastPrice - curMin
        return result