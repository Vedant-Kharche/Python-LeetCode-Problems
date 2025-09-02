class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0 
        while n: #loop until n is 0
            if n & 1: # bit present and is 1
                res += 1
            else: 
                res += 0 

            n >>= 1 # shift bits to the right

        return res 