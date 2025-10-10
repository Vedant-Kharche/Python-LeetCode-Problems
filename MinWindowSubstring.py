class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge case: if t is empty, no window possible
        if t == "":
            return ""

        # Step 1: Build frequency map for string t
        # countT will store how many times each character is required
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        # Step 2: Initialize variables
        have, need = 0, len(countT)  # have: how many chars are satisfied, need: total unique chars needed
        res, resLen = [-1, -1], float("infinity")  # stores best (left, right) indices and window length
        l = 0  # left pointer of sliding window

        # Step 3: Expand window using right pointer r
        for r in range(len(s)):
            c = s[r]
            # Add current char to window frequency map
            window[c] = 1 + window.get(c, 0)

            # If current char count matches the required count in t → one requirement satisfied
            if c in countT and window[c] == countT[c]:
                have += 1

            # Step 4: Contract window from the left when all requirements are met
            while have == need:
                # Update result if this window is smaller than previously found one
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                # Pop the leftmost character from window
                window[s[l]] -= 1
                # If removing this char makes window invalid (not enough of s[l] anymore)
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                # Move left pointer to shrink window
                l += 1

        # Step 5: Return smallest valid window substring
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""
