class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # intervals = [[1,2],[2,4],[1,4]]
        # Idea: the shorter the end of interval we save, the more space there is for coming intervals (and less likely to conflict i.e. remove)
        intervals.sort(key = lambda x: x[1]) # the lambda function means: for any given input x, we return x[1]
        prevEnd = intervals[0][1]
        res = 0
        for i in range(1, len(intervals)):
            # we are at [1,2], compare [2,4]
            if prevEnd == intervals[i][0]:
                prevEnd = intervals[i][1]
            # we are at [1,2], compare [3,4]
            elif prevEnd < intervals[i][0]:
                prevEnd = intervals[i][1]
            else: # we are at [1,3], compare [2,4]: we want to remove the one with longer end (i.e. keep our prevEnd)
                res += 1 # remove [2,4]
        return res

