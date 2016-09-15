class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict = {}
        for num in nums1:
            if num in dict:
                dict[num] = 1
            else:
                dict[num] += 1
        result = []
        for n in nums2:
            if n in dict:
                result.append(n)
                dict[num] -= 1
                if dict[num] <= 0:
                    dict.remove(num)
        return reuslt