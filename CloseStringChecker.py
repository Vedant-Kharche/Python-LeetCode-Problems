class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """

        # Initialize frequency arrays for each letter (26 lowercase English letters)
        freq1 = [0] * 26
        freq2 = [0] * 26

        # Count frequency of each character in word1
        for ch in word1:
            freq1[ord(ch) - ord('a')] += 1

        # Count frequency of each character in word2
        for ch in word2:
            freq2[ord(ch) - ord('a')] += 1

        # Check if both words have the exact same set of characters
        # If a character appears in one but not the other, they can't be "close"
        for i in range(26):
            if (freq1[i] == 0 and freq2[i] != 0) or (freq1[i] != 0 and freq2[i] == 0):
                return False

        # Sort the frequency lists
        # This checks if the counts of characters can be rearranged to match
        freq1.sort()
        freq2.sort()

        # Compare sorted frequency arrays
        # If any frequency count differs, the words are not "close"
        for i in range(26):
            if freq1[i] != freq2[i]:
                return False

        # Passed both character-set and frequency-matching tests
        return True
