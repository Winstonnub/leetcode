class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Note area formula: (Right - Left) x min (Height L or R)
        # Step 1: Initiate the variables
        l = 0
        r = len(heights) - 1
        res = 0

        # Step 2: Two pointer while loop
        while l < r:
            # Step 3: we calculate the area
            area = (r-l) * min(heights[l], heights[r])
            # Step 4: we store the current max area
            res = max(res, area)
            # Step 5: move the pointers. 
            # Moving the taller line never helps because it 
            # keeps height the same but reduce width
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
        return res

