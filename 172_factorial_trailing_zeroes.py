# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution(object):
    cache = {}

    def trailingZeroes(self, n):
        count = 0
        while n > 0:
            count += int(n / 5)
            n = int(n / 5)

        return count


s = Solution()
print(s.trailingZeroes(5))
print(s.trailingZeroes(1808548329))
