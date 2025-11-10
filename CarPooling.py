class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Sort trips by start location (t[1]) so we process them in order of pickup points
        trips.sort(key=lambda t: t[1])

        # Min-heap to keep track of ongoing trips
        # Each element in heap = [end_location, numPassengers]
        # We use the heap to know which trips end first, so we can drop passengers efficiently
        minHeap = []
        curPass = 0  # Current number of passengers in the car

        # Iterate through each trip
        for numPass, start, end in trips:
            # Before picking up new passengers, drop off those whose trip has ended
            # Pop from heap while there are trips whose end location <= current start
            while minHeap and minHeap[0][0] <= start:
                # Remove the earliest finishing trip and update passenger count
                curPass -= heapq.heappop(minHeap)[1]

            # Pick up current trip passengers
            curPass += numPass

            # If current passengers exceed car capacity → not possible
            if curPass > capacity:
                return False

            # Add current trip to heap, since these passengers are now in the car
            heapq.heappush(minHeap, [end, numPass])

        # If all trips processed without exceeding capacity, return True
        return True
