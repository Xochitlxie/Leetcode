# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        while root != None:
            p = root
            while p!= None and p.left != None:
                p.left.next = p.right
                if p.next != None:
                    p.right.next = p.next.left
                else:
                    p.right.next = None
                p = p.next
            root = root.left