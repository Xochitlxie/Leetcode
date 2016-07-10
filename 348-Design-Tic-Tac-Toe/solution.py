class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.rows = [0 * n]
        self.cols = [0 * n]
        self.diagonal = 0
        self.antiDiagonal = 0
        self.n = n
        
    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        add = 0
        if player == 1:
            add = 1
        else:
            add = -1
        
        self.rows[row] += add
        self.cols[col] += add
        
        if row == col:
            diagonal += add
        elif row == self.n - 1 - col:
            antiDiagonal += add
        
        if (abs(self.rows[row]) == self.n or abs(self.cols[col]) == self.n or abs(diagonal) == self.n or abs(antiDiagonal) == self.n):
            return player
        
# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)