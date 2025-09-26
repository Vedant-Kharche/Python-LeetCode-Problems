class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair up each car with its position and speed
        pair = [(p, s) for p, s in zip(position, speed)]
        
        # Sort cars by position in descending order (closest to target first)
        # Why? → So we process from the car nearest to the target backwards.
        pair.sort(reverse=True)
        
        stack = []  # Stack to keep track of fleets (based on arrival times)

        # Iterate through each car in reverse-sorted order
        for p, s in pair:
            # Calculate time for this car to reach target
            time = (target - p) / s
            stack.append(time)

            # If current car catches up to the fleet ahead (stack[-1] <= stack[-2]),
            # it becomes part of that fleet, so remove it from stack.
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        # Remaining elements in stack represent distinct fleets
        return len(stack)
