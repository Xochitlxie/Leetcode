class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        if not nums:
            return result
        cand1,count1,cand2,count2 = 0,0,1,0
        for n in nums:
            if n == cand1:
                count1 += 1
            elif n == cand2:
                count2 += 1
            elif count1 == 0:
                cand1,count1 = n, 1
            elif count2 == 0:
                cand2,count2 = n, 1
            else:
                count1 -= 1
                count2 -= 1
        result1 = 0
        result2 = 0
        for n in nums:
            if n == cand1:
                result1 += 1
            elif n== cand2:
                result2 += 1
        if result1 > len(nums)/3:
            result.append(cand1)
        if result2 > len(nums)/3:
            result.append(cand2)
        return result