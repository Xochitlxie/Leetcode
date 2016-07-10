class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        for update in updates:
            start = update[0]
            end = update[1]
            value = update[2]
        
        result = [0] * length
        result[start] += value
        if (end < length - 1):
            result[end + 1] -= value
        
        sum = 0
        for i in range(len(result)):
            sum += result[i]
            result[i] = sum
    
        return result