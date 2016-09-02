# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        self.dfs(root,0,result)
        return result
        
    def dfs(self,root,level,result):
        if root:
            if len(result) <= level:
                result.append([])
            result[level].append(root.val)
            self.dfs(root.left,level+1,result)
            self.dfs(root.right,level+1,result)