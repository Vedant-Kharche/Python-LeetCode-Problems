class Solution:
    def lengthOfLIS(self, nums):
        # LIS[i] will store the length of the Longest Increasing Subsequence
        # starting *at* index i
        #
        # Initialize all values to 1 because the LIS that includes only nums[i]
        # itself has length = 1
        LIS = [1] * len(nums)

        # We process the array from right to left.
        # Why? Because to compute LIS[i], we look at all future positions j > i.
        # By going right→left, all LIS[j] values are already computed.
        for i in range(len(nums) - 1, -1, -1):

            # Check all positions to the right of i.
            # If nums[j] is larger than nums[i], then nums[i] can be extended
            # into an increasing subsequence by taking nums[j].
            for j in range(i + 1, len(nums)):

                # Valid increasing step: nums[i] < nums[j]
                if nums[i] < nums[j]:

                    # Update LIS[i]:
                    # Option 1: keep old LIS[i]
                    # Option 2: extend LIS[j] → 1 (for nums[i]) + LIS[j]
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        # The answer is the maximum value in LIS[] because
        # LIS could start anywhere in the array.
        return max(LIS)
