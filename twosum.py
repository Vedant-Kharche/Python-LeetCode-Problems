class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # A will store pairs of [number, original_index]
        # We keep the index because sorting will change positions
        A = []
        
        # Enumerate gives us both index and value
        for i, num in enumerate(nums):
            A.append([num, i])

        # Sort the list based on the number (first element of each pair)
        # This allows us to use the two-pointer technique
        A.sort()

        # Initialize two pointers:
        # i -> start of the array (smallest number)
        # j -> end of the array (largest number)
        i, j = 0, len(nums) - 1

        # Continue while pointers do not cross
        while i < j:
            
            # Sum of the two numbers pointed to by i and j
            cur = A[i][0] + A[j][0]

            # If the sum matches the target
            if cur == target:
                # Return original indices (not sorted positions)
                # min/max is used to return indices in increasing order
                return [
                    min(A[i][1], A[j][1]),
                    max(A[i][1], A[j][1])
                ]

            # If current sum is too small, move left pointer right
            # (to increase the sum)
            elif cur < target:
                i += 1

            # If current sum is too large, move right pointer left
            # (to decrease the sum)
            else:
                j -= 1

        # If no pair adds up to target, return empty list
        return []
