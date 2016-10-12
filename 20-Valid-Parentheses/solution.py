class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        bracketMap = {")":"(","]":"[","}":"{"}
        for char in s:
            if len(stack) == 0:
                stack.append(char)
            elif char in bracketMap and bracketMap[char] == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0