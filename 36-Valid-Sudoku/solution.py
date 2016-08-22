class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        seen = []
        for i,row in enumerate(board):
            for j,c in enumerate(row):
                if c!= ".":
                    seen.append((c,j))
                    seen.append((i,c))
                    seen.append((i/3,j/3,c))
        return len(seen) == len(set(seen))
        
        