class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dict = {"(":")","{":"}","[":"]"}
        for char in s:
            if stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0