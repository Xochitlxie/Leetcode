class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        if s[0]  == '0':
            dp = [0] * len(s)
        else:
            dp = [1] + [0] * (len(s)-1)
        for i in range(1,len(dp)):
            if int(s[i-1]+s[i]) >= 1 and int(s[i-1] + s[i]) <=26 and int(s[i-1]+s[i]) != int(s[i]):
                dp[i] = dp[i-1] + 1
            else:
                dp[i] = dp[i-1]
        retrun dp[-1]