class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Main idea: We do backtracking index i with rows.
        # We make THREE sets.
        # col # cannot put if col c already in that set
        # posdiag # cannot put (r+c) if (r+c) already in that set
        # negdiag # cannot put (r-c) if (r-c) already in that set
        # Setup
        col = set()
        posdiag = set()
        negdiag = set()

        res = []
        curr = [["."] * n for i in range(n)] # so we have a board of empty slots
        def backtracking(r): # this time we backtrack on r
            if r == n:
                copy = ["".join(row) for row in curr]
                res.append(copy)
                return
            for c in range(n):
                if c in col or (r+c) in posdiag or (r-c) in negdiag:
                    continue
                col.add(c)
                posdiag.add(r+c)
                negdiag.add(r-c)
                curr[r][c] = 'Q'
                backtracking(r+1) # we go to next row!
                col.remove(c)
                posdiag.remove(r+c)
                negdiag.remove(r-c)
                curr[r][c] = '.'
        backtracking(0) # start backtrack at r=0
        return res
    
            

