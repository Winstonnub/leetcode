class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p,s in zip(position, speed)] # zip makes tuple list
        stack = []
        for p,s in sorted(pair)[::-1]: # sorted reverses, so first one is the rightmost car
            # add to stack
            time = (target - p) / s
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]: # if car behind reaches target in less time than right car, then they collide
                stack.pop() # as it becomes a fleet. Each entry in a stack represents a stack
        return len(stack)