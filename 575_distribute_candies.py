# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """

        max = candies.__len__() / 2
        candies_set = set(candies)
        return min(candies_set.__len__(), max)


s = Solution()
print s.distributeCandies([1, 1, 2, 3])
