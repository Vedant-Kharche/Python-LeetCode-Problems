class Solution(object):
    def tribonacci(self, n):
        # Initialize a list A of size (n+1) to store computed Tribonacci values
        A = [0] * (n + 1)

        # Handle base cases:
        # T(0) = 0, T(1) = 1, T(2) = 1
        if n == 0 or n == 1:
            return n  # T(0) = 0, T(1) = 1
        if n == 2:
            return 1  # T(2) = 1

        # Initialize base values for Tribonacci sequence
        A[0] = 0  # T(0)
        A[1] = 1  # T(1)
        A[2] = 1  # T(2)

        # Compute Tribonacci values from T(3) to T(n) using dynamic programming
        for i in range(3, n + 1):
            # T(i) = T(i-1) + T(i-2) + T(i-3)
            A[i] = A[i - 1] + A[i - 2] + A[i - 3]

        # Return the nth Tribonacci number
        return A[n]
