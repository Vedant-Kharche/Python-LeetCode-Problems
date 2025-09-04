class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Dictionary to store frequency of characters in the current window
        count = {}
        # Variable to keep track of the longest valid window (answer)
        res = 0 

        # Left pointer of the sliding window
        l = 0 

        # Expand the window with the right pointer
        for r in range(len(s)): 
            # Add current character to the count dictionary
            count[s[r]] = 1 + count.get(s[r], 0)

            # Condition: If window size - frequency of most common char > k,
            # it means we need more than k replacements → shrink the window
            while (r - l + 1) - max(count.values()) > k: 
                # Reduce the count of the leftmost character
                count[s[l]] -= 1 
                # Move left pointer to shrink window
                l += 1
            
            # Update result with the maximum window size seen so far
            res = max(r - l + 1, res)
        
        # Return the length of the longest valid substring
        return res
