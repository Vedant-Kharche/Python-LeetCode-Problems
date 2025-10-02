class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair up each car's position and speed
        # Example: [(position1, speed1), (position2, speed2), ...]
        pair = [(p, s) for p, s in zip(position, speed)]
        
        # Sort cars by starting position in descending order (closest to target first)
        # This way, we check cars from nearest to farthest
        pair.sort(reverse=True)
        
        stack = []  # will store the time each fleet (group of cars) takes to reach the target
        
        # Iterate through each car in descending position order
        for p, s in pair:  
            # Calculate time = distance / speed
            # distance = (target - p) -> how far the car is from target
            time = (target - p) / s
            stack.append(time)
            
            # If the current car catches up with the one ahead (time <= previous time),
            # then they form a fleet → merge into one (remove the current car's time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        # Remaining items in stack represent distinct fleets
        return len(stack)

