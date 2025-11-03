class Solution:

    # Encodes a list of strings into a single string
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # Add the length of the string, followed by a separator '#', then the string itself
            # Example: ["leet", "code"] → "4#leet4#code"
            res += str(len(s)) + "#" + s
            print("encoded string is", res)
        return res


    # Decodes a single encoded string back into the original list of strings
    def decode(self, s: str) -> List[str]:
        res = []   # Result list to store decoded strings
        i = 0      # Pointer to traverse the encoded string

        # Continue until we've processed the whole encoded string
        while i < len(s):
            j = i
            # Find the '#' separator to determine where the string length ends
            while s[j] != '#':
                print("j is", j)
                j += 1
            print("j is", j)

            # Convert the substring (from i to j) to an integer — this gives the length of the next string
            length = int(s[i:j])
            print("length is", length)
            print(s)

            # Move i to the start of the actual string (after '#')
            i = j + 1
            print("incrementing i is", i)

            # Compute where the string ends (start index + length)
            j = i + length
            print("incrementing j (i + length) is", j)

            # Extract the substring and append to the result list
            res.append(s[i:j])

            # Move i to the end of this word to process the next encoded part
            i = j

        return res
