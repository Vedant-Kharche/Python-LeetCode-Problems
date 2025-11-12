class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # If s1 is longer than s2, it's impossible for s2 to contain a permutation of s1
        if len(s1) > len(s2):
            return False

        # Frequency arrays for characters 'a' to 'z'
        s1Count, s2Count = [0] * 26, [0] * 26

        # Initialize the first window of size len(s1)
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1   # count chars in s1
            s2Count[ord(s2[i]) - ord('a')] += 1   # count chars in first window of s2

        # Count how many character frequencies match between s1 and the first window of s2
        matches = 0
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1

        # Start sliding the window across s2
        l = 0  # left pointer
        for r in range(len(s1), len(s2)):
            # If all 26 letters match, we found a permutation
            if matches == 26:
                return True

            # Add the new character on the right end of the window
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            # Adjust 'matches' count accordingly
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            # Remove the leftmost character (since window slides forward)
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            # Adjust 'matches' count accordingly
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1  # move window forward

        # After the loop, check one last window
        return matches == 26
