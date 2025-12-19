class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maxP keeps track of the maximum profit we can achieve so far
        maxP = 0
        
        # minBuy stores the minimum stock price seen so far (best day to buy)
        # Initially, we assume we buy on day 0
        minBuy = prices[0]

        # Iterate through each price, treating it as a potential selling price
        for sell in prices:
            # Calculate profit if we sell on this day
            # (current sell price - lowest buy price seen so far)
            maxP = max(maxP, sell - minBuy)

            # Update minBuy if we find a cheaper price to buy
            minBuy = min(minBuy, sell)

        # Return the maximum profit found
        return maxP
