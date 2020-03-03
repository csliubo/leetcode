# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution:

    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if x == 0:
            return 0
        if n == 1:
            return x
        if n == -1:
            return 1 / x
        half = self.myPow(x, int(n / 2))
        if n % 2 == 0:
            result = half * half
        else:
            result = half * half
            result = result * 1 / x if n < 0 else result * x
        return result


s = Solution()
ret = s.myPow(0.00001, 2147483647)
print(ret)
ret = s.myPow(2.10000, 3)
print(ret)
