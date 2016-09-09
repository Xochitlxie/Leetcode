# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.dfs(root,0)
        return self.res
        
    def dfs(self,root,value):
        if root:
            self.dfs(root.left,value*10+root.val)
            self.dfs(root.right,value*10+root.val)
            if not root.left and not root.right:
                self.res +=value*10+root.val