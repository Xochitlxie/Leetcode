# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result= []
        if not root:
            return result
        temp,stack,flag = [],[root],1
        while stack:
            for i in xrange(len(stack)):
                node = stack.pop(0)
                temp+=[node.val]
                if node.left:
                    stack+=[node.left]
                if node.right:
                    stack+=[node.right]
            result += [temp[::flag]]
            temp = []
            flag *= -1
        return result