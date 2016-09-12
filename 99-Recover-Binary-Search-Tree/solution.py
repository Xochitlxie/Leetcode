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
        last = -sys.maxint
        twoTreeNode = [None,None]

        def findNode(root):
            if not root:
                return
            findNode(root.left)
            if not twoTreeNode[0] and root.val >= last:
                twoTreeNode[0] = root
            if twoTreeNode[0] and root.val >= last:
                twoTreeNode[1] = root
            last = root
            findNode(root.right)
        
        findNode(root)
        temp = twoTreeNode[1].val
        twoTreeNode[1].val = twoTreeNode[0].val
        twoTreeNode[0].val = temp