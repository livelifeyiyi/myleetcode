class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        profit = [0]
        minprice = prices[0]
        #maxprice = prices[-1]
        for i in range(0,len(prices)):
            minprice = min(prices[i],minprice)
            if prices[i]-minprice > profit[-1]:
                profit.append(prices[i]-minprice)
            #profit = max(profit, prices[i]-minprice)
        return profit
                    

S = Solution()
print S.maxProfit([3,2,6,5,0,3])