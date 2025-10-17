"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Step 1: Separate and sort the start and end times of all meetings
        # This helps us track when meetings begin and end chronologically.
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        # 'res' keeps track of the maximum number of rooms needed at any point.
        # 'count' tracks the current number of ongoing meetings.
        res = count = 0

        # Two pointers:
        # 's' -> points to the next meeting start time
        # 'e' -> points to the next meeting end time
        s = e = 0

        # Step 2: Iterate through all meetings in the order of start times.
        while s < len(intervals):
            # Case 1: If the next meeting starts before the earliest meeting ends,
            # we need a new room.
            if start[s] < end[e]:
                s += 1       # Move to the next meeting start
                count += 1   # Increment current room count
            else:
                # Case 2: If the next meeting starts after or when one ends,
                # a room gets freed up.
                e += 1       # Move to the next meeting end
                count -= 1   # Decrement current room count

            # Track the maximum number of rooms in use at any time
            res = max(res, count)

        # Step 3: 'res' now holds the minimum number of meeting rooms required.
        return res
