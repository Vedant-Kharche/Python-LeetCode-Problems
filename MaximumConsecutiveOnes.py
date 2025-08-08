class Solution(object):
    def longestOnes(self, nums, k):
        """
        Sliding window approach:
        We can flip at most 'k' zeros to ones.
        Find the longest subarray containing only 1's after flipping at most k zeros.
        """

        maxlen = 0   # Stores the maximum window size
        L = 0        # Left pointer for sliding window

        # Expand the window with the right pointer R
        for R in range(len(nums)):
            # If we encounter a zero, reduce the available flips
            if nums[R] == 0:
                k -= 1

            # If we have used more than k flips, shrink the window from the left
            while k < 0: 
                if nums[L] == 0: 
                    k += 1  # Restore a flip since we're removing a zero from the window
                L += 1      # Move left pointer rightwards to shrink window

            # Update the maximum window length found so far
            maxlen = max(maxlen, R - L + 1)
            
        return maxlen
