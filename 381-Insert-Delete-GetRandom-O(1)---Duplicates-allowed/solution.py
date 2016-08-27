class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = []
        self.dict = {}

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        res = val not in self.dict
        self.list.append(val)
        if res:
            self.dict[val] = set()
        self.dict[val].add(len(self.list)-1)
        print self.list
        return res

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dict:
            return False
        else:
            outIndex,num = self.dict[val].pop(),self.list[-1]
            self.dict[num].remove(len(self.list)-1)
            self.dict[num].add(outIndex)
            self.list[outIndex] = num
            self.list.pop()
            return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return self.list[random.randint(0,len(self.list)-1)]
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()