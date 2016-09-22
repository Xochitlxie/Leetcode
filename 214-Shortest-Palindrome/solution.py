class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxLen = 0
        for i in range(len(s)):
            if s[:i+1] == s[:i+1][::-1]:
                maxLen = max(maxLen,i+1)
        return s[maxLen:][::-1] + s