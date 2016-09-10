# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.helper(range(1,n+1))
        
    def helper(self,numList):
        result = []
        if not numList:
            result.append(None)
        for i in xrange(len(numList)):
            root = TreeNode(numList[i])
            for left in self.generateTrees(numList[:i]):
                for right in self.generateTrees(numList[i+1:]):
                    root.left = left
                    root.right = right
                    result.append(root)
        return result