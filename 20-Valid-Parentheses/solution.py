class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dict = {"(":")","{":"}","[":"]"}
        for char in s:
            if len(stack) == 0 or stack[-1] != char:
                stack.append(char)
            else stack[-1] == char:
                stack.pop()
        return len(stack) == 0