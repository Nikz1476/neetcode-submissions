class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #O(n),O(1)        
        # minprice = prices[0]
        # maxprofit = 0
        # for i in range(0,len(prices)-1):
        #     if prices[i] < minprice:
        #         minprice = prices[i]
        #     else: 
        #         profit = prices[i]-minprice
        #     maxprofit = max(maxprofit,profit)
        # return maxprofit

        #sliding window
        left = 0 #buy
        right =1 #sell
        maxprofit = 0
        while (right < len(prices)):
            if prices[right] > prices[left]:
                profit = prices[right]-prices[left]
                maxprofit = max(maxprofit,profit)
            else:
                left = right
            right+=1
        return maxprofit