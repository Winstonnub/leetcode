class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        cur = [] # current solution, not necessarily will be in res
        # idea: we move i, across each number in array.
        candidates.sort() # easy to identify duplicates later
        def backtrack(i, cur, total):
            # Base case
            if total == target:
                res.append(cur.copy())
                return
            if total > target or i >= len(candidates):
                return 

            # Make the two branches
            # Go left (pick the number)
            cur.append(candidates[i])
            backtrack(i+1, cur, total+candidates[i])
            # Go back middle
            cur.pop()
            # Go right (not pick the number)
            # SPECIAL:
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1 # skip the same number. 
                #If [1,1,2,2] and want skip 1, we should skip all of 1 at once.
            backtrack(i+1, cur, total)
        backtrack(0, [], 0)
        return res

            

            


            
                
