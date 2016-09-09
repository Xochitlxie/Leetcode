# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countDepth(self,root,depth):
        if root==None:
            return depth
        else:
            leftDepth=self.countDepth(root.left,depth+1)
            rightDepth=self.countDepth(root.right,depth+1)
            return max(rightDepth,leftDepth)
    
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.countDepth(root,0)