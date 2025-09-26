class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Memoization dictionary
        # Key: (index, total)  → state of recursion
        # Value: number of ways to reach target from this state
        dp = {}

        def backtrack(i, total):
            # Base case: reached the end of the list
            if i == len(nums):
                # If total equals target → 1 valid way, else 0
                return 1 if total == target else 0

            # If already computed, return cached result
            if (i, total) in dp:
                return dp[(i, total)]

            # Two choices for each number:
            # 1. Add the current number (+nums[i])
            # 2. Subtract the current number (-nums[i])
            add = backtrack(i + 1, total + nums[i])
            subtract = backtrack(i + 1, total - nums[i])

            # Store result in dp
            dp[(i, total)] = add + subtract

            return dp[(i, total)]

        # Start recursion from index 0 and total sum 0
        return backtrack(0, 0)
