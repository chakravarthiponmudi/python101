import math
class Solution(object):
    numbers = set(['1','2','3','4','5','6','7','8','9'])
    rowset = [set(['1','2','3','4','5','6','7','8','9']) for _ in range(9)]
    colset = [set(['1','2','3','4','5','6','7','8','9']) for _ in range(9)]
    cubeset = [set(['1','2','3','4','5','6','7','8','9']) for _ in range(9)]

    def initSets(self,board):
        for i in range(9):
            for j in range(9):
                if (board[i][j] != '.'):
                    self.rowset[i].remove(board[i][j])
                    self.colset[j].remove(board[i][j])
                    cube = int(j/3) + int(i/3)*3
                    self.cubeset[cube].remove(board[i][j])
    
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.initSets(board)
        self.__solve(board,0,0)
        print(board)
    
    def __solve(self, board, i ,j):
        
        if i >= 9 :
             return True
        
        while j < 9 and board[i][j] !='.' :
            j+=1
        
        if (j>=9):
            return self.__solve(board, i+1,0)
        
        for num in self.getNumber(i,j):
            board[i][j] = num
            self.tryAndRemove(self.colset[j],num)
            self.tryAndRemove(self.rowset[i],num)
            cube = int(j/3) + int(i/3)*3
            self.tryAndRemove(self.cubeset[cube],num) 
            
            isSolved = self.__solve(board,i,j+1)
            if isSolved:
                return True
            board[i][j]='.'
            self.colset[j].add(num)
            self.rowset[i].add(num)
            self.cubeset[cube].add(num)
            
            
        return False
    
    def tryAndRemove(self,rset,n) :
        try:
            rset.remove(n)
            return True
        except:
            return False
        
    def getNumber(self,i,j):
        cube = j//3 + i//3*3
        return self.colset[j].intersection(self.rowset[i]).intersection(self.cubeset[cube]) 

        

        
s = Solution()
s.solveSudoku([[".",".",".",".",".",".",".",".","."],[".","9",".",".","1",".",".","3","."],[".",".","6",".","2",".","7",".","."],[".",".",".","3",".","4",".",".","."],["2","1",".",".",".",".",".","9","8"],[".",".",".",".",".",".",".",".","."],[".",".","2","5",".","6","4",".","."],[".","8",".",".",".",".",".","1","."],[".",".",".",".",".",".",".",".","."]])
                
                
            
            
        
        
        