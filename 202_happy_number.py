# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]

# see the wiki https://en.wikipedia.org/wiki/Happy_number

class Solution(object):
    unhappy_circule = [4, 16, 37, 58, 89, 145, 42, 20]

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
        if val in self.unhappy_circule:
            return False
        return self.isHappy(val)


s = Solution()
print s.isHappy(19)
print s.isHappy(12)
