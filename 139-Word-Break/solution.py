class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        dp = [False] * len(s)
        for i in xrange(len(s)):
            for w in wordDict:
                if w == s[i+1-len(w):i+1] and (dp[i-len(w)] or i-len(w)==-1):
                    dp[i] = True
        return dp[-1]