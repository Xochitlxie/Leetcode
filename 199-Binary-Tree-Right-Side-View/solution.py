# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def dfs(root,level):
            if not root:
                return None
            if len(result) == level:
                result.append(0)
            result[level] = root.val
            dfs(root.left,level+1)
            dfs(root.right,level+1)
        
        result = []
        dfs(root,0)
        return result
        