# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) <= 1:
            return 0
        max_profit = 0
        prices = self.remove_elements(prices)
        # print("after remove ", prices)
        if not prices or len(prices) <= 1:
            return 0
        for i in range(0, len(prices)):
            profit = self.cal_profit(prices[:i + 1]) + self.cal_profit(prices[i:])
            if profit > max_profit:
                max_profit = profit
        return max_profit

    def remove_elements(self, prices):
        new_prices = []
        direction = None
        prices_count = len(prices)
        for i in range(0, prices_count-1):
            price, next = prices[i], prices[i+1]
            if next >= price:
                if direction != 1:
                    new_prices.append(price)
                    direction = 1
            else:
                if direction != -1:
                    new_prices.append(price)
                    direction = -1
        if prices[-1] > new_prices[-1]:
            new_prices.append(prices[-1])
        return new_prices

    def cal_profit(self, prices):
        if not prices or len(prices) <= 1:
            return 0
        profit = 0
        min_price = prices[0]
        for price in prices[1:]:
            profit = max(price - min_price, profit)
            if price < min_price:
                min_price = price
        return profit


s = Solution()
r = s.maxProfit([7, 1, 5, 3, 6, 4])
print(r)
r = s.maxProfit([7, 6, 4, 3, 1])
print(r)
r = s.maxProfit([1, 2, 3, 4, 5])
print(r)
r = s.maxProfit([3, 3, 5, 0, 0, 3, 1, 4])
print(r)
r = s.maxProfit([1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 100000])
print(r)
