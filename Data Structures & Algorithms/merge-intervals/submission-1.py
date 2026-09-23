class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 1. SETUP # [1,5] and [6,7] # 6 > 5 so non overlapping
        res = []
        for start, end in sorted(intervals):
            # 2. NOT overlapping
            if not res or start > res[-1][1]: 
                res.append([start, end])
            else:
            # 3. OVERLAPPING
                res[-1][1] = max(res[-1][1], end)
        return res