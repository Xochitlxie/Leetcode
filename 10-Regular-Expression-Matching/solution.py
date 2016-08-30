class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        plist = []
        i = 0
        while i < len(p):
            if i+1 < len(p) and p[i+1] == '*':
                plist.append(p[i:i+2])
                i += 2
            else:
                plist.append(p[i])
                i += 1

        m = len(plist) + 1
        n = len(s) + 1
        
        dp = [[0]*n for i in range(m)]
        dp[0][0] = True
        
        for i in range(1, m):
            for j in range(n):
                if plist[i-1][-1] == "*":
                    if j > 0 and dp[i][j-1] and self.charMatch(plist[i-1][0], s[j-1]):
                        dp[i][j] = True
                    if dp[i-1][j]:
                        dp[i][j] = True
                else:
                    if j > 0 and dp[i-1][j-1] and self.charMatch(plist[i-1], s[j-1]):
                        dp[i][j] = True

        return dp[m-1][n-1] == 1

    def charMatch(self, c1, c2):
        return c1 == '.' or c1 == c2