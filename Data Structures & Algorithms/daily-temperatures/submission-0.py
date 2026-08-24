class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for index, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][0]: # if new temperature larger than last
                value, position = stack.pop() # e.g. 10, 1
                res[position] = index - position # e.g. 2 - 1 = 1
            stack.append((temperature, index))
        return res



''' 
# Algorithm:
[20,10,30]
res = 0 0 0
stack: (20, 0)
stack: (20, 0); (10, 1)
stack: (20, 0) (10, 1); (30, 2) -> 30 is larger than 10 -> pop 10 and add difference of 2-1
stack: (20, 0); (30, 2) -> 30 is larger than 20 -> pop 20 and add difference of 2 - 0
'''