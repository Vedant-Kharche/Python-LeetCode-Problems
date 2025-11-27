class Solution:
    def numDecodings(self, s: str) -> int:
        
        # dp is our memo/cache.
        # Key: index i in string
        # Value: number of ways to decode substring s[i:]
        dp = {len(s): 1}  
        # Why dp[len(s)] = 1?
        # Because once we reach END of string, that's 1 valid decoding path completed.

        def dfs(i):
            # If we have already computed the result for index i,
            # return it immediately from the memo (cache hit).
            if i in dp:
                return dp[i]

            # If the character starts with '0', it cannot be decoded.
            # Example: "06" is invalid.
            if s[i] == "0":
                return 0

            # ---- OPTION 1: Decode ONE character ----
            # Always valid if not '0'
            # Move to next character (i+1)
            ways = dfs(i + 1)

            # ---- OPTION 2: Decode TWO characters ----
            # Check if the next two digits form a valid number 10–26
            if (
                i + 1 < len(s) 
                and (
                    s[i] == '1'                      # 10–19 all valid
                    or (s[i] == '2' and s[i+1] in "0123456")  # 20–26 valid
                )
            ):
                ways += dfs(i + 2)

            # Store the computed number of ways in cache
            dp[i] = ways

            return ways

        # Start DFS from index 0
        return dfs(0)
