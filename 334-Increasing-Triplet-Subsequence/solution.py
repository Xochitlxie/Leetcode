class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = second = sys.maxint
        for n in nums:
            if n <= first:
                first = n
            elif n<= second:
                second = n
            self:
                return True
        return False
        
        