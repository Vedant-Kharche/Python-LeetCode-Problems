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

#TOP DOWN APPROACH
class Solution:
    def rob(self, nums: List[int]) -> int:
        # memo[i] will store the maximum amount of money that can be robbed
        # starting from house index i
        memo = [-1] * len(nums)

        def dfs(i):
            # Base case:
            # If we go beyond the last house, there is nothing left to rob
            if i >= len(nums):
                return 0

            # If we have already computed the result for this index,
            # return the stored value to avoid recomputation
            if memo[i] != -1:
                return memo[i]

            # Choice 1: Skip the current house and move to the next one
            skip_current = dfs(i + 1)

            # Choice 2: Rob the current house and skip the next house
            rob_current = nums[i] + dfs(i + 2)

            # Store the best of the two choices in memo
            memo[i] = max(skip_current, rob_current)

            return memo[i]

        # Start the recursion from the first house (index 0)
        return dfs(0)
