class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = []
        def backtrack(openN, closedN):
            # Base Case: 
            # If openN and closedN equal n!
            if openN == closedN == n:
                res.append("".join(cur)) # break list into str
                return
            # GO left (openN):
            if openN < n:
                cur.append("(")
                backtrack(openN + 1, closedN)
                cur.pop()
            # Go right (closeN)
            if closedN < openN: # no. closing is bounded by opening
                cur.append(")")
                backtrack(openN, closedN + 1)
                cur.pop()
        backtrack(0,0)
        return res
                
            
