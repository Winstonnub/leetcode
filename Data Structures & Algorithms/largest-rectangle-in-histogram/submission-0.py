class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        # Area = minHeight * length
        stack = [] # Increasing stack to easily find the left wall and right wall. Store (height, index)
                    #We do not process each bar until we found a bar  shorter than itself.
        bestArea = 0
        heights.append(0) # at the end we use 0 as the rightmost wall
        for i in range(len(heights)):
            # Formula: Max area by bar i = heights[i] x (Right shorter bar index - Left shorter bar index - 1)
            current = heights[i]
            # If our current bar is shorter than top of the stack
            while stack and current < stack[-1][0]:
                h, _ = stack.pop()
                area = h * (i - stack[-1][1] - 1) if stack else h * (i + 1 - 1)
                bestArea = max(bestArea, area)
            stack.append((current, i))
        return bestArea
            
            


            
            
