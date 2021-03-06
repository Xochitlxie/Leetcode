class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type numsSize: int
        """
        self.l = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        index,count,nums = -1,0,self.l
        for i in range(len(nums)):
            if nums[i] == target:
                if random.randint(0,count) == 0:
                    index = i
                count += 1
        return index
                

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)