class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # The "goal" represents the last index we need to be able to reach.
        # Initially, we set the goal as the last index of the array.
        goal = len(nums) - 1

        # We iterate backward through the array (starting from the 2nd last element).
        # This allows us to check whether each index can "reach" the current goal.
        for i in range(len(nums) - 2, -1, -1):

            # If the current index + its maximum jump distance
            # is greater than or equal to the current goal,
            # that means we can reach the goal from index i.
            if i + nums[i] >= goal:
                # So we update our goal to be the current index.
                # Now our new target is to see if we can reach index i from even earlier indices.
                goal = i

        # If after the loop, our goal becomes 0,
        # it means we can reach the last index starting from the first index.
        return goal == 0
