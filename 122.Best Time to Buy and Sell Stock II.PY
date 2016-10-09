class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        profit = 0
        sum_profit = 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
                profit = 0
            if profit < prices[i] - min_price:
                sum_profit -= profit
                profit = prices[i] - min_price
            else: 
                profit = 0
                min_price = prices[i]
            sum_profit += profit
            print 'min_price: '+str(min_price)+'  profit: ' + str(profit)  + '  sum_profit: ' + str(sum_profit)
        return sum_profit

S = Solution()
print S.maxProfit([6,1,3,2,4,7])