class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dict = {"}":"{","]":"[",")":"("}
        for char in s:
            if len(stack) == 0:
                stack.append(char)
            elif len(stack) > len(s)/2:
                return False
            elif char in dict and dict[char] == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0