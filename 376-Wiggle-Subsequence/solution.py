class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size,f,d = len(nums),1,1
        for i in range(1,size):
            if nums[i] > nums[i-1]:
                f = d+1
            elif nums[i] < nums[i-1]:
                d = f+1
        return min(size,max(f,d))