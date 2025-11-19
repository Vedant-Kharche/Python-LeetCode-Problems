class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()   # Sort to group duplicates together for skipping

        def dfs(i, cur, total):
            # If the current combination sums to target, add a copy to results
            if total == target:
                res.append(cur.copy())
                return

            # If total exceeds target OR we go out of bounds, stop exploring
            if total > target or i == len(candidates):
                return

            # -----------------------
            # OPTION 1: Include candidates[i]
            # -----------------------
            cur.append(candidates[i])      # Choose the element
            dfs(i + 1, cur, total + candidates[i])  # Move to next index
            cur.pop()                      # Backtrack (undo the choice)

            # -----------------------
            # OPTION 2: Skip duplicates
            # -----------------------
            # Move 'i' forward while next elements are the same
            # This ensures we only use the first instance of a number at this level
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            # -----------------------
            # OPTION 3: Skip the current number entirely
            # -----------------------
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res
