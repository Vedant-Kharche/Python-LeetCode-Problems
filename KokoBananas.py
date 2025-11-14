class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Left and right pointers for binary search.
        # Minimum speed = 1 banana/hour, maximum speed = max(piles)
        l, r = 1, max(piles)

        # Result variable to store the minimum valid eating speed
        res = r

        # Binary search to find the smallest k such that total eating time <= h
        while l <= r:
            # Middle speed (candidate speed)
            k = (l + r) // 2

            totalTime = 0
            # Calculate how many hours it takes to eat all piles at speed k
            for p in piles:
                # Each pile takes ceil(p / k) hours
                totalTime += math.ceil(float(p) / k)

            # If total hours needed is within allowed time h,
            # then k is a possible answer but we try to minimize it
            if totalTime <= h:
                res = k          # store this speed
                r = k - 1        # try to find an even smaller valid speed
            else:
                # k is too slow, so increase speed
                l = k + 1

        # res has the minimum valid eating speed
        return res
