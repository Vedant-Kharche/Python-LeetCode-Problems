class Solution(object):
    def maxArea(self, height):
        # Initialize two pointers: left (l) at start, right (r) at end
        l = 0 
        r = len(height) - 1 

        # Variable to store the maximum area found
        maxarea = 0 

        # Loop until the two pointers meet
        while l < r: 
            # Calculate the area formed between lines at l and r
            # Width = (r - l), height = min(height[l], height[r])
            area = (r - l) * min(height[l], height[r])

            # Update maximum area if current area is larger
            maxarea = max(area, maxarea)

            # Move the pointer pointing to the shorter line
            # because increasing the shorter side might give a larger area
            if height[l] > height[r]: 
                r -= 1  # Move right pointer leftwards
            else: 
                l += 1  # Move left pointer rightwards
        
        # Return the largest area found
        return maxarea
