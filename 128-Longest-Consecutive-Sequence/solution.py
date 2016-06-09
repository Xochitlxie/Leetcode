class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for num in nums:
            if num not in dict or dict[num] == 0:
                dict[num] = 1
                left = dict.get(num-1,0)
                right = dict.get(num+1,0)
                dict[num-left] = 1 + left + right
                dict[num+right] = 1 + left + right
        #for i in dict.keys():
        #    print i
        #    print dict[i]
        maxLen = 0
        for key in dict.keys():
            maxLen = max(maxLen,dict[key])
        return maxLen