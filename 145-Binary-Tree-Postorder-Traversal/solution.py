# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.postorder(root,result)
        return result
    
    def postorder(self,root,result):
        if not root:
            return
        self.postorder(root.left,result)
        self.postorder(root.right,result)
        result.append(root.val)
        return root