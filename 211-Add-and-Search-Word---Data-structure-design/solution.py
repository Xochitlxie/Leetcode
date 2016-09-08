class TrieNode(object):
    def __init__(self):
        self.word = False
        self.children = {}
        
class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.word = True
                

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.searchFrom(self.root,word)
        
    def searchFrom(self,root,word):
        for i in xrange(len(word)):
            if word[i] == "":
                for child in root.children:
                    if self.searchFrom(root.children[child],word[i+1:]):
                        return True
                return False
            elif word[i] not in root.children:
                return False
            root = root.children[word[i]]
        return root.isword

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")