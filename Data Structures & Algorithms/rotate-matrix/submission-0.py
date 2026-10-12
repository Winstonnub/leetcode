class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0]) # but also it is equal to n
        # First thing we want to do is tranpose!
        # So e.g. 4 and 2 swap meaning row 1 swap to col 1, but col 0 swap to row 0
        # STEP 1: Tranpose! (KEY: matrix[r][c] SWAP matrix[c][r])
        for r in range(0, ROWS):
            for c in range(r + 1, COLS):
                temp = matrix[r][c]
                matrix[r][c] = matrix[c][r]
                matrix[c][r] = temp
        # Step 2: Just reverse the each row! (KEY: matrix[i].reverse())
        for i in range(ROWS):
            matrix[i].reverse()



                



