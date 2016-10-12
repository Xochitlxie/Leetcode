# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        minIndex = 0
        resDict = {}
        queue = collections.deque()
        queue.append((root,0))
        while queue:
            node,i = queue.popleft()
            minIndex = min(minIndex,i)
            if i not in resDict:
                resDict[i] = []
            resDict[i].append(node.val)
            if node.left:
                queue.append((node.left,i-1))
            if node.right:
                queue.append((node.right,i+1))
        
        res = [0]*len(resDict)
        #print res,len(resDict)
        for index in resDict:
            i = index - minIndex
            res[i] = resDict[index]
        return res