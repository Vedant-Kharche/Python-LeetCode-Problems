class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Get lengths of both words
        m, n = len(word1), len(word2)

        # Memoization dictionary to store results of subproblems
        dp = {}

        # Recursive helper function to compute minimum operations
        def dfs(i, j):
            # Base case 1: if we reach the end of word1,
            # the only option is to insert the remaining characters of word2
            if i == m:
                return n - j

            # Base case 2: if we reach the end of word2,
            # we must delete the remaining characters of word1
            if j == n:
                return m - i

            # If result already computed, return it (memoization)
            if (i, j) in dp:
                return dp[(i, j)]

            # Case 1: characters match → no edit needed, move both pointers forward
            if word1[i] == word2[j]:
                dp[(i, j)] = dfs(i + 1, j + 1)

            # Case 2: characters differ → try all three edit operations
            else:
                # Option 1: delete from word1 → move i forward
                delete_op = dfs(i + 1, j)

                # Option 2: insert into word1 (i.e., move j forward in word2)
                insert_op = dfs(i, j + 1)

                # Option 3: replace character → move both forward
                replace_op = dfs(i + 1, j + 1)

                # Take the minimum among all operations and add 1 for current operation
                dp[(i, j)] = min(delete_op, insert_op, replace_op) + 1

            return dp[(i, j)]

        # Start recursion from index (0, 0)
        return dfs(0, 0)
