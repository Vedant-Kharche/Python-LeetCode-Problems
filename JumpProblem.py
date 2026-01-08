class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # The "goal" represents the last index we need to be able to reach.
        # Initially, we set the goal as the last index of the array.
        goal = len(nums) - 1

        # We iterate backward through the array (starting from the 2nd last element).
        # This allows us to check whether each index can "reach" the current goal.
        for i in range(len(nums) - 2, -1, -1):

            # If the current index + its maximum jump distance
            # is greater than or equal to the current goal,
            # that means we can reach the goal from index i.
            if i + nums[i] >= goal:
                # So we update our goal to be the current index.
                # Now our new target is to see if we can reach index i from even earlier indices.
                goal = i

        # If after the loop, our goal becomes 0,
        # it means we can reach the last index starting from the first index.
        return goal == 0

#TOP DOWN APPROACH

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Memoization dictionary
        # Stores: remaining_amount -> minimum coins needed
        memo = {}

        def dfs(amount):
            # Base case:
            # If amount becomes 0, no coins are needed
            if amount == 0:
                return 0

            # If we have already solved this subproblem,
            # return the stored result to avoid recomputation
            if amount in memo:
                return memo[amount]

            # Initialize result with a large value
            # This represents an impossible state initially
            res = 1e9

            # Try using each coin denomination
            for coin in coins:
                # Only proceed if the coin can be used
                if amount - coin >= 0:
                    # Recursively compute the minimum coins
                    # needed for the remaining amount
                    # Add 1 for the current coin used
                    res = min(res, 1 + dfs(amount - coin))

            # Store the computed result in memo
            memo[amount] = res
            return res

        # Start DFS from the target amount
        minCoins = dfs(amount)

        # If the result is still large, it means
        # the amount cannot be formed with given coins
        return -1 if minCoins >= 1e9 else minCoins
