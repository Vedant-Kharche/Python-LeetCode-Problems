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
            