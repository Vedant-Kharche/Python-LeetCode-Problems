class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Main function to solve the House Robber II problem.
        In House Robber II, houses are arranged in a circle,
        so the first and last houses cannot both be robbed.
        """

        # Case 1: Rob first house (so skip last house) → nums[:-1]
        # Case 2: Rob last house (so skip first house) → nums[1:]
        # Take the max of both cases.
        # Special case: if there's only one house, return its value directly.
        if len(nums) == 1:
            return nums[0]

        return max(
            self.helper(nums[1:]),   # Rob from 2nd house to last
            self.helper(nums[:-1])   # Rob from 1st house to second last
        )

    def helper(self, nums):
        """
        Solves the standard House Robber (linear) problem using DP.
        rob1 → max money if we rob up to the house before the previous one.
        rob2 → max money if we rob up to the previous house.
        """
        rob1, rob2 = 0, 0

        for num in nums:
            # newRob = max of:
            #   - rob1 + num: rob current house (so skip previous house)
            #   - rob2: skip current house
            newRob = max(rob1 + num, rob2)

            # Move window forward:
            rob1 = rob2      # rob1 now becomes rob2 (previous best up to house before prev)
            rob2 = newRob    # rob2 now becomes the best including current house decision

        return rob2  # Final max amount that can be robbed in this linear setup
