class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Finds the longest palindromic substring in s.
        Uses the "expand around center" technique.
        Time complexity: O(n^2), Space complexity: O(1).
        """

        # resIdx → starting index of the best palindrome found so far
        # resLen → length of the best palindrome found so far
        resIdx = 0
        resLen = 0

        # Loop through each character in the string as a potential center
        for i in range(len(s)):

            # -------- Odd-length palindrome (center at one char) --------
            l, r = i, i  # both left & right pointers start at the same char
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # If current palindrome length is greater than the best so far, update
                if (r - l + 1) > resLen:
                    resIdx = l              # store starting index
                    resLen = r - l + 1      # store length
                l -= 1  # move left pointer outwards
                r += 1  # move right pointer outwards

            # -------- Even-length palindrome (center between two chars) --------
            l, r = i, i + 1  # center is between s[i] and s[i+1]
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resIdx = l
                    resLen = r - l + 1
                l -= 1
                r += 1

        # Return the longest palindrome substring found
        return s[resIdx : resIdx + resLen]
