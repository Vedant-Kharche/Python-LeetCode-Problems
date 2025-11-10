class Solution(object):
    def largestAltitude(self, gain):
        # Initialize current altitude. Start at 0 because we start from sea level.
        altitude = 0

        # Initialize the maximum altitude. Start at 0 because initially we are at sea level.
        max_altitude = 0

        # Iterate through each net gain in altitude from the 'gain' list
        for g in gain:
            # Update the current altitude by adding the net gain for this segment
            altitude += g

            # Update the maximum altitude if the current altitude is higher
            max_altitude = max(max_altitude, altitude)

        # Return the highest altitude reached
        return max_altitude
