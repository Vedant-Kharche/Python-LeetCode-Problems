class Solution(object):
    def maxScore(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        # Step 1: Pair corresponding elements from nums1 and nums2 into tuples (n1, n2)
        # where n1 comes from nums1 and n2 from nums2
        pairs = [(n1, n2) for n1, n2 in zip(nums1, nums2)]
        
        # Step 2: Sort the pairs in descending order of n2.
        # This is because we want to consider higher values of n2 first
        # to potentially maximize the final result.
        pairs = sorted(pairs, key=lambda p: p[1], reverse=True)

        # Initialize a min-heap to keep track of the top k n1 values
        # and variables to store the running sum of selected n1 values
        # and the maximum result found so far.
        minHeap = []
        n1sum = 0
        res = 0

        # Step 3: Iterate through each (n1, n2) pair
        for n1, n2 in pairs:
            # Add current n1 to the running sum
            n1sum += n1
            # Push n1 into the min-heap
            heapq.heappush(minHeap, n1)

            # If more than k elements are in the heap, remove the smallest one
            if len(minHeap) > k:
                n1pop = heapq.heappop(minHeap)
                n1sum -= n1pop

            # If exactly k elements are in the heap, calculate potential score
            # and update result if it's the maximum seen so far
            if len(minHeap) == k:
                # Since we are iterating in descending order of n2,
                # n2 is the minimum of the current k selected values
                res = max(res, n1sum * n2)

        # Step 4: Return the maximum score found
        return res
