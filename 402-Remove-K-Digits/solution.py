class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if k == len(num):
            return "0"
        stack = []
        for i in num:
            while k>0 and stack and stack[-1] > i:
                stack.pop()
                k -= 1
            stack.append(i)
        while k:
            stack.pop()
            k -= 1
        i = 0
        while stack and i < len(stack):
            if stack[i] == "0":
                i += 1
            else:
                break
        if i == len(stack):
            return "0"
        return ('').join(stack[i:])