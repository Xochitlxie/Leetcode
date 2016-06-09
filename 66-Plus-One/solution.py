class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        num = 0
        for i in range(len(digits)):
            num = num*10 + digits[i]
        return [int(i) for i in str(num+1)]
                
"""
def plusOne(digits):
    digits[-1] += 1
    for i in range(len(digits)-1, 0, -1):
        if digits[i] != 10:
            break
        digits[i] = 0
        digits[i-1] += 1

    if digits[0] == 10:
        digits[0] = 0
        return [1] + digits
    return digits
"""
        