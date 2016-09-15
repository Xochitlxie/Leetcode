class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        if len(nums) == 1:
            return 0
        lo,hi = 0,len(nums)-2
        while lo <= hi:
            mid = lo + (hi-lo)/2
            if nums[mid] < nums[mid+1]:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo