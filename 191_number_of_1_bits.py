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
        for ch in bin(n)[2:]:
            if ch == '1':
                count += 1
        return count

s = Solution()
print s.hammingWeight(1)
print s.hammingWeight(2)
print s.hammingWeight(3)