class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        i,j,sum,minNum = 0,0,0,sys.maxint
        while j < len(nums):
            sum += nums[j]
            j += 1
            while sum > s:
                minNum = min (minNum,j-i)
                sum -= a[i]
                i += 1
        if minNum == sys.maxint:
            return 0
        else:
            return minNum