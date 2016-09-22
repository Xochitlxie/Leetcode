class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expendAroundCenter(s,left,right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1
            
        start,end = 0, 0
        for i in range(len(s)):
            len1 = expendAroundCenter(s,i,i)
            len2 = expendAroundCenter(s,i,i+1)
            maxLen = max(len1,len2)
            if (maxLen > end - start):
                start = i - (maxLen-1)/2
                end = i + maxLen/2
        return s[start:end+1]
        
        