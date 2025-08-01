class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # We convert kth largest to (len - k)th smallest
        # Because QuickSelect finds kth **smallest**, not largest
        k = len(nums) - k

        # Define quickSelect to find the kth smallest element
        def quickSelect(l, r):
            pivot = nums[r]  # Choose the rightmost element as pivot
            p = l             # Pointer for swapping smaller elements to the left

            # Partition step: move all elements <= pivot to the left
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1

            # Finally, place the pivot in its correct sorted position
            nums[p], nums[r] = nums[r], nums[p]

            # Now nums[p] is at its correct position in a sorted array
            if p > k:
                return quickSelect(l, p - 1)  # Search in left half
            elif p < k:
                return quickSelect(p + 1, r)  # Search in right half
            else:
                return nums[p]  # Found the kth smallest (originally kth largest)

        # Call quickSelect on the full array
        return quickSelect(0, len(nums) - 1)
