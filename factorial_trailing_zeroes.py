# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """

        zero_count = 0
        for i in xrange(0, n + 1, 5):
            count = 0
            num = i
            if num > 0:
                while num % 10 == 0:
                    num /= 10
                    count += 1
                while num % 5 == 0:
                    num /= 5
                    count += 1
            zero_count += count
        return zero_count

    def get_zero_count(self, n):
        count = 0
        if n > 0:
            while n % 10 == 0:
                n /= 10
                count += 1
            while n % 5 == 0:
                n /= 5
                count += 1
        return count


s = Solution()
print s.trailingZeroes(1808548329)
