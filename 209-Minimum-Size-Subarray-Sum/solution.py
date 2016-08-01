class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        i,j,sum,min = 0,0,0,sys.maxint
        while j < len(nums):
            sum += nums[j]
            j += 1
            while sum > s:
                min = min(min,j-i)
                sum -= a[i]
                i += 1
        if min == sys.maxint:
            return 0
        else:
            return min