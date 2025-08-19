class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] will represent whether substring s[i:] can be segmented into words from wordDict
        dp = [False] * (len(s)+1)

        # Base case: empty string "" (at the end) is always segmentable
        dp[len(s)] = True  

        # Traverse string backwards (from end to start)
        for i in range(len(s)-1, -1, -1):  
            # Check every word in dictionary
            for w in wordDict:
                # If word w matches substring starting at index i
                # and the rest of the string (after word) can be broken
                if (i + len(w) <= len(s) and s[i : i+len(w)] == w):  
                    dp[i] = dp[i + len(w)]   # mark dp[i] as True if dp[i+len(w)] is True
                # If dp[i] becomes True, no need to check further words
                if dp[i]:
                    break  

        # Final answer: can the entire string s[0:] be segmented?
        return dp[0]   
