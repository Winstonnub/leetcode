class Solution:
    def trap(self, height: List[int]) -> int:
        # Two ingredients: make a prefix maximum and postfix maximum. The minimum of both MINUS the height at i is the water it can hold
        # water at i = min(leftMax, rightMax) - height[i]
        # 1. Make the prefix and postfix maximum
        currMax = 0
        res = 0
        prefix = []
        for i in range(0, len(height)):
            currMax = max(currMax, height[i])
            prefix.append(currMax)
        postfix = deque([])
        currMax = 0
        for i in range(len(height)-1, -1, -1):
            currMax = max(currMax, height[i])
            postfix.appendleft(currMax)
        # Then we go through each height!
        for i in range(0, len(height)):
            leftMax, rightMax = prefix[i], postfix[i]
            res += min(leftMax, rightMax) - height[i]
        return res