class Solution:
    def generateParenthesis(self, n):
        # res[k] will store all valid combinations of parentheses with k pairs
        res = [[] for _ in range(n+1)]
        res[0] = [""]   # Base case: 0 pairs -> only the empty string is valid

        # Build solutions bottom-up for each number of pairs from 0..n
        for k in range(n + 1):
            # Partition k pairs into two groups:
            # i pairs inside the first parentheses "()" + (k-i-1) pairs outside
            for i in range(k):
                # Iterate over all valid sequences of i pairs
                for left in res[i]:
                    # Iterate over all valid sequences of (k-i-1) pairs
                    for right in res[k-i-1]:
                        # Form a new sequence: "(" + left + ")" wraps the 'inside'
                        # then add 'right' as the sequence after it
                        res[k].append("(" + left + ")" + right)

        # Return all valid combinations for n pairs
        return res[-1]
