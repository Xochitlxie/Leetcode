# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.minIndex = 0
        def bfs(node,n):
            if node == None:
                return
            self.minIndex = min(self.minIndex,n)
            if n not in resDict:
                resDict[n] = []
            resDict[n].append(node.val)
            bfs(node.left,n-1)
            bfs(node.right,n+1)
        
           
        resDict = {}
        bfs(root,0)
        res = [[] for _ in resDict]
        #print res
        for i in resDict:
            3print i,resDict[i]
            index = i - self.minIndex 
            res[index] = resDict[i]
        return res