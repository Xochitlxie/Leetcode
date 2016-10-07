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
            if k>0 and stack and stack[-1] > i:
                stack.pop()
                k -= 1
            stack.append(i)
        #print stack
        i = 0
        while stack:
            if stack[i] == "0":
                i += 1
            else:
                break
        return ('').join(stack[i:])