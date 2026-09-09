class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Permutation
        res = []
        cur = []
        # Base case:
        def backtrack(i, cur):
            if i >= len(nums):
                res.append(cur[:])
                return
            # For each option, choose then unchoose
            for num in nums:
                # choose node 1
                if not num in cur:
                    cur.append(num)
                    backtrack(i+1, cur)
                    cur.pop()
        backtrack(0, cur)
        return res
            
        