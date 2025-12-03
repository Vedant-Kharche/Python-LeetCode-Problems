class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        # This function MERGES two sorted halves of the array
        def merge(arr, L, M, R):
            # Copy left half and right half into temporary arrays
            left = arr[L:M+1]      # from index L to M
            right = arr[M+1:R+1]  # from index M+1 to R
            
            # i -> pointer for original array
            # j -> pointer for left array
            # k -> pointer for right array
            i, j, k = L, 0, 0

            # Compare elements from left and right and place smaller into arr
            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]   # take from left
                    j += 1
                else:
                    arr[i] = right[k]  # take from right
                    k += 1
                i += 1  # move main array pointer forward

            # If any elements remain in left array, copy them
            while j < len(left):
                arr[i] = left[j]
                j += 1
                i += 1

            # If any elements remain in right array, copy them
            while k < len(right):
                arr[i] = right[k]
                k += 1
                i += 1

        # This function RECURSIVELY divides the array
        def mergeSort(arr, l, r):
            # Base case: if only one element, it's already sorted
            if l >= r:
                return

            # Find mid point
            m = (l + r) // 2

            # Recursively sort left half
            mergeSort(arr, l, m)

            # Recursively sort right half
            mergeSort(arr, m + 1, r)

            # Merge the two sorted halves
            merge(arr, l, m, r)

        # Start merge sort on the full array
        mergeSort(nums, 0, len(nums) - 1)

        # Return the sorted array
        return nums
