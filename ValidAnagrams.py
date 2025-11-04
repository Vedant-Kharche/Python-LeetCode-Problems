class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Step 1: Quick length check
        # If strings have different lengths, they can't be anagrams.
        if len(s) != len(t):
            return False 

        # Step 2: Create two hash maps (dictionaries)
        # counts -> stores frequency of each character in string s
        # countt -> stores frequency of each character in string t
        counts, countt = {}, {}

        # Step 3: Iterate through both strings simultaneously
        for i in range(len(s)):
            # For string s: increment the count of the character s[i]
            counts[s[i]] = 1 + counts.get(s[i], 0)
            
            # For string t: increment the count of the character t[i]
            countt[t[i]] = 1 + countt.get(t[i], 0)

        # Step 4: Compare frequency maps
        # For every character in s, check if its count matches in t
        for char in counts:
            if counts[char] != countt.get(char, 0):
                # If any count doesn't match, s and t are not anagrams
                return False 

        # Step 5: If all counts match, strings are anagrams
        return True
