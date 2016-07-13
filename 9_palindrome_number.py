# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x < 10:
            return True
        limit = 10
        count = 1
        while (x >= limit):
            count += 1
            limit *= 10
        limit /= 10

        for i in range(0, count / 2):
            first_one = x / limit
            x = x % limit
            last_one = x % 10
            x = x / 10
            limit /= 100
            if first_one != last_one:
                return False
        return True


s = Solution()
print s.isPalindrome(0)
print s.isPalindrome(10)
print s.isPalindrome(123)
print s.isPalindrome(12321)
print s.isPalindrome(-12321)
