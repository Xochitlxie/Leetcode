class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l=len(nums)
        start,end = 0,l
        while start < end:
            if nums[start] == 0:
                nums[start],nums[end] = nums[end],nums[start]
                end -= 1
            else:
                start += 1