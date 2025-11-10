class Solution(object):
    def reverseWords(self, s):
        # Split the string into a list of words using default whitespace delimiter
        # s.split() automatically removes extra spaces and splits by any whitespace
        S = s.split()[::-1]  # Reverse the list of words using slicing [::-1]
        
        # Initialize an empty string to store the reversed words
        new = ''
        
        # Loop through each word in the reversed list
        for i in S:
            # Append each word followed by a space
            new += i + ' '
        
        # Remove any trailing spaces from the final string
        new = new.strip()
        
        # Return the reversed words as a single string
        return new

