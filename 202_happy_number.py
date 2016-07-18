# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        if n == 1:
            return True
        digits = []
        while n > 0:
            digit = n % 10
            if digit:
                digits.append(digit)
            n /= 10
        val = 0
        for digit in digits:
            val += digit * digit
        if val == 1:
            return True

        return self.isHappy(val)


s = Solution()
print s.isHappy(19)
print s.isHappy(12)
