class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        neg_inf = -(2**31-1)
        
        minValue = neg_inf
        stack = []
        for num in preorder:
            if num < minValue:
                return False
            
            while len(stack) > 0 and stack[-1] < num:
                minValue = stack.pop()
            stack.append(num)
        return True
        