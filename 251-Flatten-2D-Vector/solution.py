class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.i = self.j = 0
        self.vec2d = vec2d

    def next(self):
        """
        :rtype: int
        """
        ret = self.vec2d[self.i][self.j]
        if self.j == len(self.vec2d[self.i]) - 1:
            self.i += 1
            if self.i <= len(self.vec2d)-1:
                while not self.vec2d[self.i]:
                    self.i += 1
            self.j = 0
        elif self.j < len(self.vec2d[self.i]) - 1:
            self.j += 1
            
    def hasNext(self):
        """
        :rtype: bool
        """
        if self.i >  len(self.vec2d)-1:
            return False
        else:
            return True
                

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())