# -*- coding:utf-8 -*-


__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]

import sys

from math import log


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """

        max_three_power = pow(3, int(log(sys.maxint, 3)))
        return n > 0 and max_three_power % n == 0


s = Solution()
print s.isPowerOfThree(0)
print s.isPowerOfThree(1)
print s.isPowerOfThree(2)
print s.isPowerOfThree(3)
print s.isPowerOfThree(4)
print s.isPowerOfThree(6)
print s.isPowerOfThree(8)
print s.isPowerOfThree(9)
print s.isPowerOfThree(12)
print s.isPowerOfThree(18)
print s.isPowerOfThree(27)
