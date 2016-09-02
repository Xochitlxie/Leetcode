# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return self.getNode(postorder,0,inorder,0,len(inorder))
    
    def getNode(self,postorder,pstart,inorder,istart,length):
        if length == 0:
            return None
        root = TreeNode(postorder[pstart+length-1])
        print root.val
        leftLen = inorder.index(postorder[pstart+length-1])-istart
        root.left = self.getNode(postorder,pstart,inorder,istart,leftLen)
        root.right = self.getNode(postorder,pstart+leftLen,inorder,istart+leftLen+1,length-leftLen-1)
        return root