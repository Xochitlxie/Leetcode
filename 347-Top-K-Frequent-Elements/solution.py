from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        most_item = Counter(nums).most_commin(k)
        result = []
        for i in most_item:
            result.append(i[0])
        return result
    