class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        heights,hMap,result = [],{},[]
        for p in people:
            if p[0] not in hMap:
                heights.append(p[0])
                hMap[p[0]] = []
            hMap[p[0]].append(p[1])
        for h in sorted(heights)[::-1]:
            position = sorted(hMap[h])
            for j in position:
                result.insert(j,(h,j))
        return result