class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Step 1: Sort intervals by start time (default sort on first element, then second).
        intervals.sort()
        
        res = 0                       # Counter for intervals to remove
        prevEnd = intervals[0][1]     # Track the end of the previous non-overlapping interval
        
        # Step 2: Iterate through the remaining intervals
        for start, end in intervals[1:]:
            if start >= prevEnd:
                # Case 1: No overlap
                # Update prevEnd to current interval's end
                prevEnd = end
            else:
                # Case 2: Overlap detected
                res += 1  # Remove one interval (greedy choice)
                
                # Keep the interval with the smaller end to maximize space for future intervals
                prevEnd = min(end, prevEnd)
        
        # Step 3: Return total removals needed
        return res
