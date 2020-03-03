# -*- coding:utf-8 -*-
from typing import List

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution:
    def candy(self, ratings: List[int]) -> int:
        if not ratings:
            return 0
        ratings_count = len(ratings)
        candies = [1 for _ in range(ratings_count)]
        for i in range(1, ratings_count):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        for i in range(ratings_count - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and candies[i] <= candies[i+1]:
                candies[i] = candies[i + 1] + 1

        return sum(candies)


s = Solution()
# l = [2, 2, 2]
# ret = s.candy(l)
# print(ret)
# l = [1, 2, 2]
# ret = s.candy(l)
# print(ret)
# l = [1, 0, 2]
# ret = s.candy(l)
# print(ret)
l = [9, 8, 6, 77, 28, 19, 30, 22]
# l = [9, 8, 6, 6, 77, 28, 19, 30, 30, 22]
l=[1,3,4,5,2]
ret = s.candy(l)
print(ret)
