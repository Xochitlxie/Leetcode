class Solution(object):
    def longestValidParentheses(self, strs):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for s in strs:
            dic[tuple(sorted(s))] = dic.get(tuple(sorted(s)),[]) + [s]
        return [sorted(item) for item in dic.values()]