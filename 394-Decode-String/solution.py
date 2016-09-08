class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        if not s:
            stack.append(["",1])
        num = ""
        for ch in s:
            if ch.isdigit():
                num += ch
            elif ch == "[":
                stack.append(["",int(num)])
                num = ""
            elif ch == "]":
                s,c = stack.pop()
                newString = s*c
                stack[-1][0] += newString
            else:
                stack[-1][0] += ch
        return stack[0][0]