class Solution:
    def rob(self, nums: List[int]) -> int:
        # If the input list is empty, there's nothing to rob
        if not nums:
            return 0
        
        # If there's only one house, rob it
        if len(nums) == 1:
            return nums[0]

        # Create a DP array where dp[i] will store the maximum amount that can be robbed from the first i+1 houses
        dp = [0] * len(nums)

        # Initialize base cases:
        dp[0] = nums[0]  # Robbing only the first house
        dp[1] = max(nums[0], nums[1])  # Rob either the first or second house, whichever has more money

        # Fill the dp array for the rest of the houses
        for i in range(2, len(nums)):
            # For each house, decide: 
            # - Either rob this house and add its value to dp[i-2] (which is the max loot till house i