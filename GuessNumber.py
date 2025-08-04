# The guess API is provided externally and returns:
#   -1 if your guess is higher than the target number,
#    1 if your guess is lower than the target number,
#    0 if your guess is correct.

class Solution(object):
    def guessNumber(self, n):
        # Initialize the search range between 1 and n (inclusive)
        l, r = 1, n

        # Use binary search to efficiently find the correct number
        while True:
            # Calculate the middle point of the current search range
            m = (l + r) // 2

            # Call the provided guess API to check the middle value
            res = guess(m)

            if res > 0:
                # If the guess is too low (picked number is higher),
                # move the left boundary up to search the upper half
                l = m + 1

            elif res < 0:
                # If the guess is too high (picked number is lower),
                # move the right boundary down to search the lower half
                r = m - 1

            else:
                # If guess is correct, return the number
                return m
