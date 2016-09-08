class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.dic = {}
        for word in set(dictionary):
            if word:
                if len(word) <= 2:
                    if word not in self.dic:
                        self.dict[word] = set()
                        self.dict[word].add(word)
                else:
                    abb = word[0]+str(len(word)-2)+word[-1]
                    if abb in self.dic:
                        self.dic[abb].add(word)
                    else:
                        self.dic[abb] = set()
                        self.dic[abb].add(word)

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        if word in self.dic:
            return False
        else:
            if len(word) <= 2:
                return False
            else:
                wordAbb = word[0]+str(len(word)-2)+word[-1]
                if wordAbb in self.dic:
                    if word in self.dic[wordAbb] and len(self.dic[wordAbb]) > 1:
                        return False
                    elif word not in self.dic[wordAbb]:
                        return False
        return True
        
    

# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")