class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        solution = []
        if len(s) < 2:
            return False
        for i in range(len(s)-1):
            if s[i]=="+" and s[i+1]=="+":
                solution.append(s[:i]+"--"+s[i+2:])
        print solution
        for string in solution:
            if not self.win(string):
                return True
        return False
            
    def win(self,string):
        for i in range(1,len(string)):
            if string[i-1:i+1] == "++":
                if not self.win(string[:i-1]+"--"+string[i+1:]):
                    return True
        return False
        
    # O(n) + O(n^2)