class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        # For each row, generate hashset
        row = [set() for i in range(ROWS)]
        col = [set() for i in range(COLS)]
        cell = [set() for i in range(9)] # 123, 456, 789

        def findCell(r,c):
            if r <= 2:
                if c <= 2: return 0
                if c <= 5: return 1
                if c <= 8: return 2
            if r <= 5:
                if c <= 2: return 3
                if c <= 5: return 4
                if c <= 8: return 5
            if r <= 8:
                if c <= 2: return 6
                if c <= 5: return 7
                if c <= 8: return 8

        for r in range(ROWS):
            for c in range(COLS):
                cellIndex = findCell(r,c)
                if board[r][c] == ".":
                    continue
                if board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in cell[cellIndex]:
                    return False
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                cell[cellIndex].add(board[r][c])  
        return True


            

#lookup:
# if r <= 2: 123
# if r <= 5: 456
# if r <= 8: 789

# if c <= 2: 147
# if c <= 5: 258
# if c <= 8: 369

            
        
    
# For each cell, for each row, for each column, create a hashset (so 9 + 9 + 9 = 27)
