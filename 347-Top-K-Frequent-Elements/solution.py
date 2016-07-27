from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        numLen = k
        frequency = {}
        for num in nums:
            frequency[num] = frequenct.get(num,0) + 1
        
        bucket = [None] * (len(nums)+1)
        for (num,freq) in frequency.items():
            if bucket[freq] == None:
                bucket[freq] = []
            bucket[freq].append(num)
        
        result = []
        for i reversed(range(len(nums) + 1)):
            if k > 0:
                if bucket[i] != None:
                    result.extend(bucket[i])
                    k -= 1
            else:
                break
        
        return result[0:numLen]