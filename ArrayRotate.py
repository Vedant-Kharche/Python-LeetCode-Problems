class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)      # Length of the array
        
        # Reduce k in case it is larger than n
        # Rotating n times gives the same array
        k %= n             

        # 'count' tracks how many elements have been moved so far
        count = 0          

        # 'start' is the starting index of each cycle
        start = 0          

        # Continue until all n elements are placed in correct position
        while count < n:
            
            current = start           # Current index in this rotation cycle
            prev = nums[start]        # Store the value to be moved

            while True:
                # Calculate the next index where the current value should go
                next_idx = (current + k) % n

                # Swap values:
                # - Place 'prev' in its rotated position
                # - Store displaced value back into 'prev'
                nums[next_idx], prev = prev, nums[next_idx]

                # Move to the next index in the cycle
                current = next_idx

                # One element successfully placed
                count += 1

                # If we have returned to the start index,
                # the current cycle is complete
                if start == current:
                    break

            # Move to next index to begin a new cycle
            start += 1
