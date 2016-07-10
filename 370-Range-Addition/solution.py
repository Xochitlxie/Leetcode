class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        result = [0] * length
        for update in updates:
            result[update[0]] += update[2]
            if (update[1] < length - 1):
                result[update[1] + 1] -= update[2]
        
        sum = 0
        for i in range(len(result)):
            sum += result[i]
            result[i] = sum
    
        return result