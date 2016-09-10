class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last, curr, steps = 0, 0, 0
        for i, ei in enumerate(nums):
            if i > last:
                last = curr
                steps += 1
            curr = max(curr, i + ei)
        return steps