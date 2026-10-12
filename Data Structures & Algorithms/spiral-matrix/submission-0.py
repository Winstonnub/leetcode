class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        # Keep 4 pointers: top, down, left, right
        # We stop when top < down
        ROWS, COLS = len(matrix), len(matrix[0])
        top = 0
        down = ROWS - 1
        left = 0
        right = COLS - 1
        res = []
        while top <= down and left <= right:
            # First Row
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            if top > down or left > right: break
            # Col
            for i in range(top, down + 1):
                res.append(matrix[i][right])
            right -= 1
            for i in range(right, left - 1, -1):
                res.append(matrix[down][i])
            down -= 1
            if top > down or left > right: break
            for i in range(down, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        return res
