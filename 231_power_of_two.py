# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        left_part = bin(n)[3:]
        if left_part == '0' * left_part.__len__():
            return True
        return False


s = Solution()
print s.isPowerOfTwo(1)
print s.isPowerOfTwo(2)
print s.isPowerOfTwo(3)
print s.isPowerOfTwo(4)
print s.isPowerOfTwo(5)
print s.isPowerOfTwo(6)
print s.isPowerOfTwo(7)
print s.isPowerOfTwo(8)
