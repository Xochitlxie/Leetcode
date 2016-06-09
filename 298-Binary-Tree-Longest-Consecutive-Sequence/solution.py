# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        maxLen = [0]
        if root:
            self.dfs(root,1,maxLen)
        return maxLen[0]
        
    def dfs(self,root,length,maxLen):
        if not root.left and not root.right:
            maxLen[0] = max(maxLen[0],length)
            return
        if root.left:
            if root.left.val == root.val + 1:
                self.dfs(root.left,length+1,maxLen[0])
            else:
                maxLen[0] = max(maxLen[0],length)
                self.dfs(root.left,1,maxLen)
        if root.right:
            if root.right.val == root.val + 1:
                self.dfs(root.right,length+1,maxLen)
            else:
                maxLen[0] = max(maxLen[0],length)
                self.dfs(root.right,1,maxLen)
        