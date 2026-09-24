class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:

        left = []
        right = []
        start = newInterval[0]
        end = newInterval[1]
        
        for i in range(len(intervals)):
            if intervals[i][1] < newInterval[0]:
                left.append(intervals[i])
            elif intervals[i][0] > newInterval[1]:
                right.append(intervals[i])
            elif intervals[i][0] <= newInterval[1] and intervals[i][1] >= newInterval[0]:
                start = min(intervals[i][0], start)
                end = max(intervals[i][1], end)

        return left + [[start, end]] + right