# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        answer = TreeNode(None)
        if root == None:
            return None
        answer.val = root.val
        answer.left = self.invertTree(root.right)
        answer.right = self.invertTree(root.left)
        return answer