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
        profit = 0
        for i, price in enumerate(prices[:-1]):
            if price < prices[i + 1]:
                profit += prices[i + 1] - price
        return profit


s = Solution()
r = s.maxProfit([7, 1, 5, 3, 6, 4])
print(r)
r = s.maxProfit([7, 6, 4, 3, 1])
print(r)
r = s.maxProfit([1, 2, 3, 4, 5])
print(r)
