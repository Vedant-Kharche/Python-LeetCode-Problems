class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # If combined lengths of s1 and s2 don't match s3,
        # it's impossible for s3 to be an interleaving of them.
        if len(s1) + len(s2) != len(s3):
            return False

        # Memoization dictionary to store intermediate results.
        # Key: (i, j) — indices in s1 and s2
        # Value: Boolean indicating if s3[k:] can be formed from s1[i:] and s2[j:]
        dp = {}

        # Recursive helper function using Depth-First Search + memoization
        def dfs(i, j, k):
            # Base Case: If we've reached the end of s3,
            # return True only if both s1 and s2 are also fully used.
            if k == len(s3):
                return (i == len(s1)) and (j == len(s2))

            # If this state has already been computed, return the cached result.
            if (i, j) in dp:
                return dp[(i, j)]

            # Variable to store the result for the current state.
            res = False

            # Option 1: If the current character of s1 matches s3,
            # move forward in both s1 and s3 and recursively check.
            if i < len(s1) and s1[i] == s3[k]:
                res = dfs(i + 1, j, k + 1)

            # Option 2: If Option 1 fails (res is False) and
            # the current character of s2 matches s3,
            # move forward in both s2 and s3 and check recursively.
            if not res and j < len(s2) and s2[j] == s3[k]:
                res = dfs(i, j + 1, k + 1)

            # Store the computed result in dp to avoid recomputation.
            dp[(i, j)] = res
            return res

        # Start recursion from the beginning of all strings.
        return dfs(0, 0, 0)
