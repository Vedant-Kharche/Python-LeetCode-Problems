"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Step 1: Sort the meeting intervals based on their start times.
        # This ensures we can easily compare each meeting with the next one.
        intervals.sort(key=lambda i: i.start)

        # Step 2: Iterate through the sorted list to check for overlaps.
        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]  # Previous meeting
            i2 = intervals[i]      # Current meeting

            # Step 3: If the previous meeting's end time is greater than
            # the current meeting's start time, the meetings overlap.
            # This means a person cannot attend both meetings.
            if i1.end > i2.start:
                return False

        # Step 4: If no overlaps were found, all meetings can be attended.
        return True
