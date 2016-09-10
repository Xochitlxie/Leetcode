class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxJump = []
        for i in range(len(nums)):
            maxJump.append(i+nums[i])
        i = len(maxJump)-2
        lastStep = len(maxJump)-1
        while i > 0:
            if maxJump[i] >= lastStamp:
                lastStamp = i
            i -= 1
        return lastStep == 0
                
            