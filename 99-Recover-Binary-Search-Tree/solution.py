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
        self.last = TreeNode(-sys.maxint)
        self.twoTreeNode = [None,None]

        def findNode(root):
            if not root:
                return
            findNode(root.left)
            print root.val
            if not self.twoTreeNode[0] and root.val <= self.last.val:
                self.twoTreeNode[0] = self.last
            if self.twoTreeNode[0] and root.val <= self.last.val:
                self.twoTreeNode[1] = root
            print self.twoTreeNode
            self.last = root
            findNode(root.right)
        
        findNode(root)
        print self.twoTreeNode[0].val
        print self.twoTreeNode[1].val
        temp = self.twoTreeNode[1].val
        self.twoTreeNode[1].val = self.twoTreeNode[0].val
        self.twoTreeNode[0].val = temp