class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)   # Total count of elements (so numbers should be from 0..n)

        # Start with n, because the full range is 0..n (inclusive n)
        xorr = n

        # XOR all indices and values together
        for i in range(n):
            # XOR with index i and nums[i]
            # Doing this ensures every number from 0..n cancels out if present,
            # leaving behind only the missing number
            xorr ^= i ^ nums[i]

        return xorr  # The leftover value is the missing number
