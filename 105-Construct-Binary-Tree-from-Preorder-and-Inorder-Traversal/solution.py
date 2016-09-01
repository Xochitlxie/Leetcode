# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.getNode(preorder,0,inorder,0,len(preorder))
        
    def getNode(self,preorder,pstart,inorder,istart,length):
        if length == 0:
            return None
        root = TreeNode(preorder[pstart])
        leftLen = inorder.index(preorder[pstart],istart,istart + length) - istart
        root.left = self.getNode(preorder, pstart + 1, inorder, istart, leftLen)
        root.right = self.getNode(preorder, pstart + leftLen + 1, inorder, istart + leftLen + 1, length - leftLen - 1)
        return root