import sys
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = sys.maxint
        dict = {}
        for i in xrange(len(s)):
            dict[s[i]] = dict.get(s[i],[])
            dict[s[i]].append(i)
        for char in dict.keys():
            if len(dict[char]) <= 1:
                result = min(result,dict[char][0])
        if result == sys.maxint:
            return -1
        else:
            return result