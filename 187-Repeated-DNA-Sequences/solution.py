class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        if len(s) <= 10:
            return result
        dict = {}
        for i in range(10,len(s)+1):
            dict[s[i-10:i]] = dict.get(s[i-10:i],0) + 1
            print i,dict[s[i-10:i]],s[i-10:i]
        for key in dict.keys():
            if dict[key] >= 2:
                result.append(key)
        return result