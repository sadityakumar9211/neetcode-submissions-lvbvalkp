class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Its just puzzle that you have to practice. Its nothing else. Makes you stronger and better in interviews.
        # If I want to sell on this day. 
        
        # This is a one pass solution. 
        # There is another brute force solution if we fix the 
        # buying days and not selling days.

        maxProfit = 0 # no transactions made
        minPrice = prices[0] # prices can't be negative

        for i, price in enumerate(prices):
            maxProfit = max(maxProfit, price - minPrice)
            minPrice = min(minPrice, price)
        
        return maxProfit
