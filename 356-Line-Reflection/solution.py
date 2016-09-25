class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if len(points) <= 1: return True
        mid = (min(points)[0] + max(points)[0])*1.0/2
        count = {}
        for point in points:
            if point[0] == mid:
                continue
            elif point[0] < mid:
                count[(mid-point[0],point[1])] = count.get((mid-point[0],point[1]),0) + 1
            else:
                count[(point[0] - mid,point[1]) = count.get((mid-point[0],point[1]),0) -1
        for key in count:
            if count[key] != 0:
                return False
        return True