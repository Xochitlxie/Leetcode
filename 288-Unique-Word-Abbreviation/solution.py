class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.dic = set()
        for word in set(dictionary):
            if word:
                if len(word) <= 2:
                    self.dic.add(word)
                else:
                    self.dic.add(word[0]+string(len(word)-2)+word[-1])

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        if word in self.dic:
            return False
        else:
            return True
        


# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")