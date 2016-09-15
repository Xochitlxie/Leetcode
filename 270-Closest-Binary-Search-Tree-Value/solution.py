# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        a = root.val 
        if target < a:
            kid = root.left
        else:
            kid = root.right
        if not kid:
            return a
        b = self.closetValue(kid,target)
        return (a,b)[abs(a-target) > abs(b-target)]