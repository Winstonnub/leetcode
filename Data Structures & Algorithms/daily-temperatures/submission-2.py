class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp: # stack has (i, temp)
                updateIndex, updateTemp = stack.pop()
                result[updateIndex] = i - updateIndex
            stack.append((i, temp))
        return result