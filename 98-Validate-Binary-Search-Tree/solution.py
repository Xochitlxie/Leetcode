# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root != None:
            if root.left.val > root.val or root.right.val < root.val:
                return False
            else:
                if self.isValidBST(root.left) and self.isValidBST(root.right):
                    return True