class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If the lengths differ, they can never be anagrams
        if len(s) != len(t):
            return False 

        # Dictionaries to count the frequency of characters in both strings
        counts, countt = {}, {}

        # Iterate through each character in both strings simultaneously
        for i in range(len(s)):
            # Increase the count for the current char in s
            counts[s[i]] = 1 + counts.get(s[i], 0)
            # Increase the count for the current char in t
            countt[t[i]] = 1 + countt.get(t[i], 0)

        # Compare character counts from s against those in t
        for char in counts:
            # If a character’s frequency in s is different from t → not an anagram
            if counts[char] != countt.get(char, 0):
                return False 

        # If all characters match in frequency, s and t are anagrams
        return True
