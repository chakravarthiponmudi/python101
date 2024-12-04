import math
class Solution(object):
    numbers = set(['1','2','3','4','5','6','7','8','9'])
    
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.__solve(board,0,0)
        print(board)
    
    def __solve(self, board, i ,j):
        
        if i >= 9 :
             return True
        
        while j < 9 and board[i][j] !='.' :
            j+=1
        
        if (j>=9):
            return self.__solve(board, i+1,0)
        
        for num in self.getNumber(board,i,j):
            if self.isValid(board,i,j,num):
                board[i][j] = num
                isSolved = self.__solve(board,i,j+1)
                if isSolved:
                    return True
                board[i][j]='.'
            
        return False
    
    def getNumber(self,board,i,j):
        s= set()
        [s.add(board[i][c]) for c in range(9) if board[i][c] != '.']
        for r in range(9):
            if board[r][j] != '.':
                s.add(board[r][j])
        cubeRow = int(math.floor(i/3)*3)
        cubeCol = int(math.floor(j/3)*3)
        
        for r in range(cubeRow, cubeRow+3):
            for c in range(cubeCol, cubeCol+3):
                if (board[r][c]!='.'):
                    s.add(board[r][c])
        
        return list(self.numbers.difference(s))
            
            
        
    
    def isValid(self,board, i ,j, n):
        if n in board[i]:
            return False
        
        for r in range(9):
            if n == board[r][j]:
                return False
        cubeRow = int(math.floor(i/3)*3)
        cubeCol = int(math.floor(j/3)*3)
        
        for r in range(cubeRow, cubeRow+3):
            for c in range(cubeCol, cubeCol+3):
                if (n==board[r][c]):
                    return False;
        
        return True
        
s = Solution()
s.solveSudoku([[".",".",".",".",".",".",".",".","."],[".","9",".",".","1",".",".","3","."],[".",".","6",".","2",".","7",".","."],[".",".",".","3",".","4",".",".","."],["2","1",".",".",".",".",".","9","8"],[".",".",".",".",".",".",".",".","."],[".",".","2","5",".","6","4",".","."],[".","8",".",".",".",".",".","1","."],[".",".",".",".",".",".",".",".","."]])
                
                
            
            
        
        
        