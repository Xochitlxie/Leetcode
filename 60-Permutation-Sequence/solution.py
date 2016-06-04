class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        list = [str(i) for i in range(1,n+1)]
        stringList = []
        self.dfs(k-1,n,list,stringList)
        return "".join(stringList)
        
    def dfs(self,k,n,list,string):
        if len(list) == 0:
            return
        factorial = 1
        for i in range(1,n):
            factorial *= i
        j = k/factorial
        k = k%factorial
        string.append(list[j])
        self.dfs(k,n-1,list[:j]+list[j+1:],string)
        
    #O(1) since the maximum number of n is 9