class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        set_zero = []
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    set_zero.append((r,c))
        # We now have all positions!
        for r,c in set_zero:
            for i in range(0, COLS):
                matrix[r][i] = 0
            for i in range(0, ROWS):
                matrix[i][c] = 0
                    
