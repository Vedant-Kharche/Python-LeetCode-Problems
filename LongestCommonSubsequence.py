class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Let m = len(text1), n = len(text2).
        # dp[i][j] will store the length of the LCS of text1[i:] and text2[j:].
        # We allocate (m+1) x (n+1) so that dp[m][*] and dp[*][n] = 0 (base cases:
        # an empty suffix has LCS length 0).
        dp = [[0 for j in range(len(text2) + 1)]
                 for i in range(len(text1) + 1)]

        # We fill the table bottom-up. By iterating i from m-1 down to 0 and
        # j from n-1 down to 0, the entries dp[i+1][j], dp[i][j+1], and
        # dp[i+1][j+1] (which we depend on) are already computed.
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                # If the current characters match, the LCS of text1[i:] and text2[j:]
                # includes this character and is 1 + LCS of the remaining suffixes:
                # dp[i][j] = 1 + dp[i+1][j+1]
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    # If characters don't match, the LCS is the max between:
                    #  - skipping the char in text2: dp[i][j+1]
                    #  - skipping the char in text1: dp[i+1][j]
                    # This implements the recurrence: dp[i][j] = max(dp[i][j+1], dp[i+1][j])
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        # The answer for the whole strings is LCS(text1[0:], text2[0:]) = dp[0][0]
        return dp[0][0]
