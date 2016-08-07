class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        count = 0
        pairs = ["00","11","69","88","96"]
        for i in range(len(low),len(high)+1):
            self.dfs(low,high,["0"]*i,0,i-1)
        return count
        
    def dfs(self.low,high,c,left,right):
        if left > right:
            s = "".join(c)
            if (len(s) == len(low) and int(s) < int(low)) or (len(s) == len(high) and int(s) > int(high)):
                return
            count += 1
            return
        for p in pairs:
            c[left] = p[0]
            c[right] = p[1]
            if len(c) != 1 and c[0] == 0:
                continue
            if left < right or (left == right and p[0] == p[1]):
                self.dfs(low,high,c,left+1,right-1)

        