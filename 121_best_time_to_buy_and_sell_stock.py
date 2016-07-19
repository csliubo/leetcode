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
        if not prices:
            return 0
        if prices.__len__() <= 1:
            return 0
        min = prices[0]
        max_profit = 0
        for price in prices:
            if min > price:
                min = price
            profit = price - min
            if profit > max_profit:
                max_profit = profit
        return max_profit


s = Solution()
print s.maxProfit([7, 1, 5, 3, 6, 4])
