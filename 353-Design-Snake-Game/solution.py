import collections
class SnakeGame(object):
    
    
    def __init__(self, width,height,food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.dirs = {"U":(0,-1),"D":(0,1),"L":(-1,0),"R":(1,0)}
        self.food = food
        self.width = width
        self.height = height
        self.foodIndex = 0
        self.snake = collections.deque()
        self.snake.append((0,0))
        self.body = set([(0,0)])
        
    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        
        tail = self.snake.popleft()
        print tail
        self.body.remove(tail)
        if not self.snake:
            head = tail
        else:
            head = self.snake[-1]
        nx = head[0] + self.dirs[direction][0]
        ny = head[1] + self.dirs[direction][1]
        if nx < 0 or ny < 0 or nx>= self.width or ny >= self.height or (nx,ny) in self.body:
            return -1
        self.snake.append((nx,ny))
        print self.snake
        self.body.add((nx,ny))
        if self.foodIndex < len(self.food) and nx == self.food[self.foodIndex][1] and ny == self.food[self.foodIndex][0]:
            self.foodIndex += 1
            self.snake.appendleft(tail)
            self.body.add(tail)
        return len(self.snake) - 1

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)