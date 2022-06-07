class BestTimetoBuyandSellStock:
    """
    Desc:
        # 121
        You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
    Link: 
        https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
    Notes:
        - sliding window
    """

    # bruce force
    # Time: O(n^2)
    # Space: O(1)
    def solution1():
        pass


    # sliding windows - store max profit while updating cheaper buy prices moving forward 
    # Time: O(n)
    # Space: O(1)
    def solution2(self, prices):
        curr_profit, maxx_profit = 0, 0
        l, r = 0, 0 # l = buy, r = sell 

        while r < len(prices):
            curr_profit = prices[r] - prices[l]
            maxx_profit = max(curr_profit, maxx_profit)
            # update buy if cheaper than prev buy   
            if prices[r] < prices[l]:
                l = r
            r += 1
        
        return maxx_profit