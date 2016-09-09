class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.helper(root,result)
        return result
        
    def helper(self,root,result):
        if root:
            self.helper(root.left,result)
            result.append(root.val)
            self.helper(root.right,result)