class Solution:
    def countSubstrings(self, s: str) -> int:
        # Initialize a counter for the number of palindromic substrings
        res = 0 

        # Iterate through each character in the string
        for i in range(len(s)):
            # Check for odd-length palindromes centered at s[i]
            l = r = i  # left and right pointers start at the same center
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1  # found a palindrome
                l -= 1    # expand to the left
                r += 1    # expand to the right

            # Check for even-length palindromes centered between s[i] and s[i+1]
            l = i
            r = i + 1  # center is between two characters
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1  # found a palindrome
                l -= 1    # expand to the left
                r += 1    # expand to the right

        # Return the total count of palindromic substrings
        return res
