class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights) - 1
        res = 0
        while l < r:
            area = min(heights[l], heights[r])*(r-l)
            res = max(res, area)
            if heights[l] > heights[r]:
                r -= 1
            elif heights[l] <= heights[r]:
                l += 1
        return res
            