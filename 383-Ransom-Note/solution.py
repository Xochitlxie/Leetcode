class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dict = {}
        for i in magazine:
            dict[i] = dict.get(i,0) + 1
        for j in ransonNote:
            if j in dict.keys():
                dict[j] -= 1
                if dict[j] < 0:
                    return False
            else:
                return False
        return True