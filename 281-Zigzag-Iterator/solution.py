class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.stack = [list for list in (v1,v2) if list]
        
    def next(self):
        """
        :rtype: int
        """
        list = self.stack.pop(0)
        node = list.pop(0)
        if list:
            self.stack.append(list)
        return node

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) != 0

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())