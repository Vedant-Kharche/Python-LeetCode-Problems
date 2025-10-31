import heapq

class MedianFinder:
    def __init__(self):
        # Initialize two heaps:
        # self.small -> Max Heap (simulated using negative values)
        # self.large -> Min Heap
        #
        # Goal:
        # - 'small' contains the smaller half of numbers
        # - 'large' contains the larger half of numbers
        # - Both heaps are kept balanced in size (difference ≤ 1)
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        """
        Adds a number into the data structure while keeping both heaps balanced.
        """
        
        # Step 1: Decide which heap to push the new number into
        # If 'large' is not empty and 'num' is greater than the smallest element of 'large',
        # it belongs to the larger half → push to 'large' (min heap)
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            # Otherwise, push to 'small' (max heap simulated by storing negative numbers)
            heapq.heappush(self.small, -1 * num)

        # Step 2: Rebalance the heaps if needed
        # The size difference between heaps should never exceed 1
        # Case 1: 'small' has more than one extra element
        if len(self.small) > len(self.large) + 1:
            # Move the largest element from 'small' to 'large'
            val = -1 * heapq.heappop(self.small)  # get the max value from 'small'
            heapq.heappush(self.large, val)

        # Case 2: 'large' has more than one extra element
        if len(self.large) > len(self.small) + 1:
            # Move the smallest element from 'large' to 'small'
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        """
        Returns the median of all numbers added so far.
        """
        
        # Case 1: 'small' has more elements → median is top of 'small'
        if len(self.small) > len(self.large):
            return -1 * self.small[0]

        # Case 2: 'large' has more elements → median is top of 'large'
        elif len(self.large) > len(self.small):
            return self.large[0]

        # Case 3: Heaps are equal in size → median is the average of both tops
        return (-1 * self.small[0] + self.large[0]) / 2.0
