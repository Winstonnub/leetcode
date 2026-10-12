"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Want a way to find the meeting room that ends the earliest
        # e.g. [0,30] in use,
        # then we compare [0,30] and [5,10] #since start time 5 is earlier than 30, we have to make a new room 
        # then we compare [15,20] and (WHO? the earliest room! n this case is [5,10]), since start time 15 is later than 10, we can use this room :D (since we sorted, there is no one queueing earlier in front of us to use this room as well)
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x.start) # Sort since we have a queue to use the rooms :)
        occupied_rooms = [intervals[0].end]
        for i in range(1, len(intervals)):
            prevEnd = occupied_rooms[0] # Tells you when is the earliest time a room is free, e.g 30
            # if we are [32,50]
            if intervals[i].start >= prevEnd: # we don't need to make our own room! Just use that :D
                heapq.heappop(occupied_rooms)
            heapq.heappush(occupied_rooms, intervals[i].end) # Otherwise, we make a new room and add it to our room priority queue
        return len(occupied_rooms)

                


            