class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Create a Counter object to count how many times each number appears in nums
        count = Counter(nums)
        
        # Initialize an empty list to store the result (numbers appearing > n/3 times)
        res = []

        # Loop through each unique number (key) in the counter
        for key in count:
            # Check if the count of this number is greater than one-third of the total length
            # According to the problem, we need to find all elements that appear more than ⌊n/3⌋ times
            if count[key] > len(nums) // 3:
                # If true, add this number to the result list
                res.append(key)

        # Return the final list of majority elements
        return res
