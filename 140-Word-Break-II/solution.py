class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        def dfs(s,value):
            if self.check(s,wordDict):
                if len(s) == 0:
                    ans.append(value[1:])
                for i in range(1,len(s)+1):
                    if s[:i] in wordDict:
                        dfs(s[i:],value+' '+s[:i])
        ans = []
        dfs(s,'')
        return ans

    def check(self, s, dict):
        dp = [False for i in range(len(s)+1)]
        dp[0] = True
        for i in range(1, len(s)+1):
            for k in range(0, i):
                if dp[k] and s[k:i] in dict:
                    dp[i] = True
        return dp[len(s)]
        