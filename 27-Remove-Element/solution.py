class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        start, end = 0, len(nums)-1
        while start <= end:
            if nums[start] != val:
                start += 1
            else:
                nums[start],nums[end] = nums[end],nums[start]
                end -= 1
        return start