class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []  # this will store all valid combinations that sum up to target

        # dfs(i, cur, total):
        # i     -> current index in nums we're exploring
        # cur   -> current combination being built
        # total -> sum of the numbers in 'cur'
        def dfs(i, cur, total):
            # ✅ Base case: if total == target, we found a valid combination
            if total == target:
                res.append(cur.copy())  # add a copy of cur (to avoid mutation issues)
                return

            # ❌ If out of bounds or total already exceeds target, stop exploring
            if i >= len(nums) or total > target:
                return

            # 🔹 Choice 1: include nums[i] in the combination
            cur.append(nums[i])  
            dfs(i, cur, total + nums[i])  # stay on same index (i) since we can reuse the number
            cur.pop()  # backtrack (remove last element to try other possibilities)

            # 🔹 Choice 2: skip nums[i] and move to the next index
            dfs(i + 1, cur, total)

        # start DFS from index 0 with empty combination and sum = 0
        dfs(0, [], 0)
        return res
