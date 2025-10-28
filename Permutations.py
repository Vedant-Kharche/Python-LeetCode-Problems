class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Start with a list containing an empty permutation
        perms = [[]]

        # Loop through each number in the input list
        for num in nums:
            # Temporary list to store new permutations formed by inserting the current number
            new_perms = []

            # For each existing permutation in the list
            for p in perms:
                # Try inserting the current number 'num' at every possible position
                for i in range(len(p) + 1):
                    # Make a copy of the current permutation
                    p_copy = p.copy()

                    # Insert the current number at position 'i'
                    p_copy.insert(i, num)

                    # Add this new permutation to the temporary list
                    new_perms.append(p_copy)

            # Update perms with the newly generated permutations
            perms = new_perms

        # After processing all numbers, 'perms' will contain all possible permutations
        return perms
