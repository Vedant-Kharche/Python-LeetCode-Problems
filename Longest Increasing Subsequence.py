class Solution:
    def lengthOfLIS(self, nums):
        n = len(nums)

        # memo[i][j+1] stores the LIS value starting from index i
        # when the previous element chosen is at index j
        # We use j+1 because j can be -1 (meaning no previous element chosen)
        memo = [[-1] * (n + 1) for _ in range(n)]

        def dfs(i, j):
            """
            dfs(i, j) = length of LIS using nums[i:] given previous chosen index j.
            j = -1 means no previous number included yet.
            """

            # Base case: reached end of array
            if i == n:
                return 0

            # Memoized result: return if already computed
            # We use j+1 because j can be -1
            if memo[i][j + 1] != -1:
                return memo[i][j + 1]

            # Option 1: Skip nums[i]
            LIS = dfs(i + 1, j)

            # Option 2: Take nums[i] IF it forms an increasing order
            if j == -1 or nums[j] < nums[i]:
                # If we take nums[i], add 1 to LIS count
                LIS = max(LIS, 1 + dfs(i + 1, i))

            # Store in memo
            memo[i][j + 1] = LIS
            return LIS

        # Start from index 0 with no previous element chosen (j = -1)
        return dfs(0, -1)
