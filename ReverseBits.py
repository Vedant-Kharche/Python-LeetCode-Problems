class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0  # This will hold the reversed bits result
        
        # Loop through all 32 bits (since input is a 32-bit unsigned integer)
        for i in range(32):
            # Extract the i-th bit of n
            # (n >> i) shifts n right by i bits, then & 1 isolates the last bit
            bit = (n >> i) & 1  
            
            # Place this extracted bit in the reversed position
            # If the bit was at index i, in reversed form it goes to (31 - i)
            res += (bit << (31 - i))  
        
        # Return the final reversed integer
        return res
