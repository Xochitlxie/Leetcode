# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result = []
        if not root:
            return result
        self.dfs(root,result,[],sum)
        return result
        
    def dfs(self,root,result,curList,sum):
        if not root.left and not root.right and root.val == sum:
            curList.append(root.val)
            result.append(curList)
            return
        if root.left:
            self.dfs(root.left,result,curList+[root.val],sum-root.val)
        if root.right:
            self.dfs(root.right,result,curList+[root.val],sum-root.val)