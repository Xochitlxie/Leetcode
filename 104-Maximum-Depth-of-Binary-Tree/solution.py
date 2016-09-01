# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.countDepth(root,0)
        
    def countDepth(self,node,depth):
        if not node:
            return depth
        else:
            leftDepth = self.countDepth(node.left,depth+1)
            rightDepth = self.countDepth(node.right,depth+1)
            return max(leftDepth,rightDepth)