class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        self.wordIndex = {}
        for i in xrange(len(words)):
            word = words[i]
            if word in self.wordIndex:
                self.wordIndex[word].append(i)
            else:
                self.wordIndex[word] = [i]

    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        a,b = self.wordIndex[word1],self.wordIndex[word2]
        m,n,i,j,res = len(a),len(b),0,0,sys.maxsize
        while i < m and j < n:
            res = min(res,abs(a[i]-b[j]))
            if a[i] < b[j]:
                i += 1
            else:
                j += 1
        return res
# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")