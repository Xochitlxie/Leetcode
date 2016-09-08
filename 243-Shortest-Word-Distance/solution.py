class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        size = len(words)
        index1,index2 = size,size
        result = size

        for i in xrange(len(words)):
            if words[i] == word1:
                index1 = i
                result = min(result,abs(index1-index2))
            elif words[i] == word2:
                index2 = i
                result = min(result,abs(index1-index2))
        return result
                