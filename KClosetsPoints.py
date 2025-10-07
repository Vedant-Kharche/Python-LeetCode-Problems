class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Initialize an empty list to store [distance, x, y] for each point
        minHeap = []
        
        # Step 1: Calculate the squared distance of each point from the origin (0, 0)
        for x, y in points:
            # Euclidean distance formula = sqrt(x^2 + y^2)
            # We can skip the square root since we're only comparing distances
            dist = (x ** 2) + (y ** 2)
            # Store as [distance, x, y] so that heapq can sort based on distance
            minHeap.append([dist, x, y])

        # Step 2: Convert the list into a min-heap (smallest distance at the top)
        heapq.heapify(minHeap)

        # Step 3: Extract the k smallest-distance points
        res = []
        while k > 0:
            # Pop the smallest element (closest point) from the heap
            dist, x, y = heapq.heappop(minHeap)
            # Append only the coordinates (x, y) to the result
            res.append([x, y])
            k -= 1  # Decrease the count of remaining closest points to find

        # Step 4: Return the list of k closest points
        return res