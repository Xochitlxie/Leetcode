class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.i, self.j = 0,0
        self.vec = vec2d

    def next(self):
        """
        :rtype: int
        """
        ret = self.vec[self.i][self.j]
        self.j += 1
        return ret
            
    def hasNext(self):
        """
        :rtype: bool
        """
        while self.i < len(self.vec):
            if self.col < len(self.vec[self.i]):
                return True
            self.col = 0
            self.row += 1
        return False
                

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())