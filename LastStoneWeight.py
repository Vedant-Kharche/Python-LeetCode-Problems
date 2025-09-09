class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Convert all stone weights to negative values
        # Because Python's heapq is a min-heap, negating lets us simulate a max-heap
        stones = [-s for s in stones]
        heapq.heapify(stones)  # Turn list into a heap (O(n))

        # Keep smashing stones until at most one is left
        while len(stones) > 1:
            first = heapq.heappop(stones)   # heaviest stone (most negative)
            second = heapq.heappop(stones)  # second heaviest

            # If they are not equal, push the "difference" back as a new stone
            if second > first:   # remember: more negative = lighter, so second > first means |second| < |first|
                heapq.heappush(stones, first - second)

        # If no stones left, return 0
        stones.append(0)   # ensures at least one element to return
        return abs(stones[0])   # convert back to positive since we stored negatives