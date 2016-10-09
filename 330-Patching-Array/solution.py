class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        miss,added,i = 0,0,0
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                i += 1
                miss += nums[i]
            else:
                miss += miss
                added += 1
        return added