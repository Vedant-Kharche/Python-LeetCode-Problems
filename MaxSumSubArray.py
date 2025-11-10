class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize maxSub with the first element
        # (at least one number must be included in the subarray)
        maxSub = nums[0]
        
        # Variable to keep track of the current running sum
        curSum = 0 
        
        # Iterate through each number in the array
        for n in nums: 
            # If the current sum becomes negative,
            # reset it to 0 (start fresh from current number)
            if curSum < 0: 
                curSum = 0
            
            # Add the current number to the running sum
            curSum += n 
            
            # Update maxSub with the larger of:
            # - current maxSub
            # - current running sum
            maxSub = max(maxSub, curSum)
        
        # Return the maximum subarray sum found
        return maxSub
