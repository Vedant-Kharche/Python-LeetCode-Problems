class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums: 
            if n in count.keys():
                count[n] += 1
            else: 
                count[n] = 1 
        
        arr = []
        sorted_dict = dict(sorted(count.items(), key=lambda item: item[1], reverse = True))
        print("sorted dict", sorted_dict)

        #time complexity = O(n + nlogn)
        #space complexity = O(n)
        return list(sorted_dict.keys())[:k]
            
##Bucket Sort Approach

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Step 1: Count frequency of each number
        # Example: nums = [1,1,1,2,2,3]
        # count = {1:3, 2:2, 3:1}
        count = {}
        
        # Step 2: Create buckets where index = frequency
        # Maximum frequency possible is len(nums)
        # freq[i] will store numbers that appear exactly i times
        freq = [[] for i in range(len(nums) + 1)]

        # Populate the frequency map
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # Step 3: Place numbers into their respective frequency buckets
        # Example:
        # freq[3] = [1]
        # freq[2] = [2]
        # freq[1] = [3]
        for num, cnt in count.items():
            freq[cnt].append(num)

        # Step 4: Collect top k frequent elements
        res = []

        # Traverse buckets from highest frequency to lowest
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                
                # Stop once we have k elements
                if len(res) == k:
                    return res
