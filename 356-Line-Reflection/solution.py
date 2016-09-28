class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if len(points) <= 1: return True
        mid = (min(points)[0] + max(points)[0])*1.0/2
        leftBucket = set()
        rightBucket = set()
        for point in points:
            if point[0] == mid:
                continue
            elif point[0] < mid:
                leftBucket.add((mid-point[0],point[1]))
            else:
                rightBucket.add((point[0] - mid,point[1]))
        if len(leftBucket)!= len(rightBucket):
            return False
        while leftBucket:
            ele = leftBucket.pop()
            if ele not in rightBucket:
                return False
        return True