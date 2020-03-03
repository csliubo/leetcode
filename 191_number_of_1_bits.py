# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            if n & 1 == 1:
                count += 1
            n >>= 1
        return count


s = Solution()
print(s.hammingWeight(1))
print(s.hammingWeight(2))
print(s.hammingWeight(3))
