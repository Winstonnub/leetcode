class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Idea: Understand the matrix is just sorted numbers!
        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, ROWS*COLS - 1
        while l <= r:
            m = l + (r - l) // 2
            row, col = m // COLS, m % COLS # which place in col, and which row depends on how many slots (cols)
            if matrix[row][col] < target:
                l = m + 1
            elif matrix[row][col] > target:
                r = m - 1
            else:
                return True
        return False


'''
        # Algorithm:
            # We search rows from left to right.
            # For each pass,
            # we check whether the rightmost element is smaller than target
            #   If yes, we go next
            #   If not (rightmost is larger than target),
            #   Then we perform binary search in that list # BUT THIS IS NOT O log(m*n)
        for r in matrix:
            if r[-1] < target:
                continue
            elif r[-1] == target:
                return True
            else: # target might be within this
                hashset = set(r)
                if target in hashset:
                    return True
                else:
                    return False
        return False
'''