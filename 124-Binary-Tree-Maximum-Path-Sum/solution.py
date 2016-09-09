# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        largest = [-2**31]
        self.helper(root,largest)
        return largest[0]
        
    def helper(self, root, largest):
        if root == None:
            return 0
        left = self.helper(root.left, largest)
        right = self.helper(root.right, largest)
        largest[0] = max(
            largest[0], 
            left + right + root.val, 
            left + root.val, 
            right + root.val, 
            root.val
        )
        return max(max(left, right) + root.val, root.val)
        