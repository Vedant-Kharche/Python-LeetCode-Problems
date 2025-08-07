class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []  # List to store the result

        # Loop through all numbers from 0 to n
        for i in range(n + 1):
            # Convert number to binary using bin(i)
            # bin(i) returns a string like '0b101', so we slice off the '0b' using [2:]
            # count('1') counts the number of 1's in the binary string
            count = bin(i)[2:].count('1')

            # Append the count to the result list
            res.append(count)

        return res  # Return the list of counts
