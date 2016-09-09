# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
    
        # using Morris Traversal of BT
        
        node = root
        while node:
            if node.left:
                pre = node.left
                while pre.right:
                    pre = pre.right
                pre.right = node.right
                node.right = node.left
                node.left = None
            node = node.right