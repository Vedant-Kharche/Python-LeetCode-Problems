class Solution(object):
    def maxVowels(self, s, k):
        # Create a set of vowels for quick lookup
        vowels = set('aeiou')
        
        # Current count of vowels in the current window
        count = 0
        
        # Maximum number of vowels found in any window
        max_count = 0

        # Step 1: Initialize the first window of size k
        for i in range(k):
            if s[i] in vowels:
                count += 1
        # Set the initial max_count as the count from the first window
        max_count = count

        # Step 2: Slide the window from position k to end of string
        for i in range(k, len(s)):
            # Add the new character entering the window
            if s[i] in vowels:
                count += 1
            # Remove the character going out of the window
            if s[i - k] in vowels:
                count -= 1
            # Update the max_count if the current window has more vowels
            max_count = max(max_count, count)

        # Step 3: Return the maximum number of vowels found in any window
        return max_count
