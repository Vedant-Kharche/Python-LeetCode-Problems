class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair up each car's position with its speed
        pair = [(p, s) for p, s in zip(position, speed)]
        
        # Sort cars by position in descending order (farthest along the road first)
        # This way, we process cars from closest to the target back towards the start
        pair.sort(reverse=True)

        stack = []  # This will store the time each "fleet" takes to reach the target

        for p, s in pair:  # iterate from car closest to target to farthest
            # Time for this car to reach the target
            time = (target - p) / s
            stack.append(time)

            # If the current car catches up to the one in front (or is slower),
            # they form a fleet, and the current car's time is not a new fleet.
            # stack[-1] = time of current car
            # stack[-2] = time of fleet in front
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                # Current car joins the fleet ahead, so its individual time is irrelevant
                stack.pop()

        # The number of remaining times in the stack = number of fleets
        return len(stack)

