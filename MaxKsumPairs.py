# Count frequency of each number in the array
        count = Counter(nums)

        # This will store the number of valid k-sum pairs
        operations = 0

        # Iterate through each unique number in the counter
        for num in count:
            # Find the complement needed to make sum = k
            complement = k - num

            # Case 1: num pairs with itself (example: k=6, num=3)
            if num == complement:
                # Each pair needs two same numbers
                # Example: count[3] = 5 → we can form 2 pairs
                operations += count[num] // 2

            # Case 2: num pairs with a different number
            # Use num < complement to avoid double counting pairs
            elif num < complement and complement in count:
                # The number of pairs is limited by the smaller frequency
                # Example: count[1]=3, count[4]=2 → only 2 pairs possible
                operations += min(count[num], count[complement])

        # Return total number of k-sum pairs
        return operations