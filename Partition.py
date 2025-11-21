class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Sum of all numbers
        total = sum(nums)

        # If total sum is odd, we cannot split into two equal subsets
        if total % 2 != 0:
            return False

        # We want to find a subset that sums to half the total
        target = total // 2
        n = len(nums)

        # memo[i][t] will store whether it's possible to reach sum 't'
        # using elements from index i onward.
        # Values: -1 = not computed, 0 = False, 1 = True
        memo = [[-1] * (target + 1) for _ in range(n + 1)]

        def dfs(i, target):
            """
            dfs(i, target): can we form 'target' using nums[i:] ?
            """

            # Base case: We successfully formed the required sum
            if target == 0:
                return True

            # Base case: No more numbers OR target went negative
            if i >= n or target < 0:
                return False

            # If already computed, use memoized result
            if memo[i][target] != -1:
                return memo[i][target]

            # OPTION 1: Skip current number
            skip = dfs(i + 1, target)

            # OPTION 2: Take current number
            take = dfs(i + 1, target - nums[i])

            # Store the result: True or False
            memo[i][target] = skip or take

            return memo[i][target]

        # Start recursion at index 0 with required target
        return dfs(0, target)
