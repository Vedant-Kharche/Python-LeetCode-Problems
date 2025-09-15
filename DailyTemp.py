class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Initialize the result list with 0s. 
        # Each index i will store the number of days until a warmer temperature occurs.
        res = [0] * len(temperatures)
        
        # Stack to keep track of temperatures and their indices
        # We'll store pairs: (temperature, index)
        stack = []

        # Iterate over the list of temperatures with index i and temperature t
        for i, t in enumerate(temperatures):
            # Check if the current temperature t is greater than the last temperature in the stack
            # This means we have found the next warmer day for the temperature at stack[-1]
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()  # Remove the last temperature from the stack
                # Calculate the number of days until a warmer temperature
                res[stackInd] = i - stackInd

            # Add the current temperature and its index to the stack
            # We haven't found a warmer day for this temperature yet
            stack.append((t, i))
        
        # Return the result list
        return res
