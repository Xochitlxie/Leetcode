class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def bisect_left(l,x,hi):
            if hi >= 0 and x > l[hi]:
                return hi+1
            i,j = 0,hi
            while i < j:
                mid = i + (j-i)/2
                if x > l[mid]:
                    i = mid + 1
                else:
                    j = mid
            return i
            
        tails = [None] * len(nums)
        size = 0
        for x in nums:
            i = bisect_left(tails,x,size-1)
            print i
            tails[i] = x
            size = max(size,i+1)
            print size
        return size
        