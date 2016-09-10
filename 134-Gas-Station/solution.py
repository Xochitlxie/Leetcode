class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start = len(gas) - 1
        end = 0
        sum = gas[start] - cost[start]
        while start > end:
            if sum >= 0:
                sum += gas[end] - cost[end]
                end += 1
            else:
                start -= 1
                sum += gas[start] - cost[start]
        return (start,-1)[sum<0]