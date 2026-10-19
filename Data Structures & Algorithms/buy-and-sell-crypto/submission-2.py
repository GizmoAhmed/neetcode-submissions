class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        p = 0

        for i in range(len(prices) + 2):
            if r > len(prices) - 1 or prices[l] > prices[r]:
                l = r
                r = l + 1
            else:
                if prices[r] - prices[l] > p:
                    p = prices[r] - prices[l]
                r += 1

        return p



        
        