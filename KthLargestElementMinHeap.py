class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Store the given list as a min-heap and keep k for later reference
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)   # Convert nums into a valid min-heap in O(n) time

        # Ensure the heap only keeps the k largest elements
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)   # Remove the smallest element until size == k

    def add(self, val: int) -> int:
        # Add the new value into the min-heap
        heapq.heappush(self.minHeap, val)

        # If heap grows beyond k, remove the smallest element
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        # The root of the heap (smallest in heap) is the k-th largest overall
        return self.minHeap[0]