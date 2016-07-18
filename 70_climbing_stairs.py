# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]

import math


def comb(n, r):
    '''
    取组合数
    :param n:
    :param r:
    :return:
    '''
    f = math.factorial
    return f(n) / f(r) / f(n - r)


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 1
        if n <= 2:
            return n
        ret = 0
        for i in range(0, n / 2 + 1):
            two_count = i
            one_count = n - (i * 2)
            ret += comb(one_count + two_count, two_count)
        return ret


s = Solution()
print s.climbStairs(1)
print s.climbStairs(2)
print s.climbStairs(4)
print s.climbStairs(10)
print s.climbStairs(11)
