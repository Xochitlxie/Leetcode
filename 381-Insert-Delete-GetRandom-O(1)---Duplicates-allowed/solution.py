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
        self.dict[val].add(len(self.dict)-1)
        return res

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dict:
            i,newVal = self.dict[val].pop(),self.list[-1]
            if len(self.dict[val]) == 0:
                del self.dict[val]
            self.list[i] = newVal
            self.dict[newVal].add(i)
            self.dict[newVal].remove(len(self.list)-1)
            self.list.pop()
            return True
            
        return False

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