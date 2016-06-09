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
        count = []
        if root:
            self.dfs(root,1,count)
        maxLen = 0
        print count
        for i in count:
            maxLen = max(maxLen,i)
        return maxLen
        
    def dfs(self,root,length,count):
        if not root.left and not root.right:
            count.append(length)
            return
        if root.left:
            if root.left.val == root.val + 1:
                self.dfs(root.left,length+1,count)
            else:
                count.append(length)
                self.dfs(root.left,1,count)
        if root.right:
            if root.right.val == root.val + 1:
                self.dfs(root.right,length+1,count)
            else:
                count.append(length)
                self.dfs(root.right,1,count)
        