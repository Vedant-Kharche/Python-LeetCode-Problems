class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # We assume strs has at least one string.
        # We will compare each character of the first string with all other strings.

        # Loop through each character index of the first string
        for i in range(len(strs[0])):

            # Now compare this character position with every string in the list
            for s in strs:
                
                # Two cases break the common prefix:
                # 1. If the current index i is beyond the length of the current string `s`
                #    → that means this string is shorter, so the prefix must stop here.
                # 2. If the character at index i of `s` is not equal to the character at the same
                #    index of the first string → mismatch, so prefix ends.
                if i == len(s) or s[i] != strs[0][i]:
                    # Return the prefix of the *current string* s from [0:i]
                    # (All characters up to—but NOT including—index i)
                    return s[:i]

        # If we never returned inside the loop, it means the entire first string
        # is a common prefix for all the strings.
        return strs[0]
