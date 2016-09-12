# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        firstElement = None
        secondElement = None
        preElement = TreeNode(-sys.maxint)

        traverse(root)
        temp = firstElement.val
        firstElement.val = secondElement.val
        secondElement.val = temp
            
        def traverse(node):
            if not node:
                return
            traverse(node.left)
            if not firstElement and preElement.val >= node.val:
                firstElement = preElement
            if firstElement and preElement.val >= node.val:
                secondElement = root
            preElement = root
            traverse(node.right)