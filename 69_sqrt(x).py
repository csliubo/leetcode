# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution(object):
    def mySqrt2(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        if x <= 3:
            return 1
        nums = [x for x in range(2, x // 2 + 1)]

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            mid_val = nums[mid]
            mid_val_square = mid_val * mid_val
            if mid_val_square == x:
                return mid_val
            if mid_val_square < x < nums[mid + 1] * nums[mid + 1]:
                return mid_val
            if x > mid_val_square:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def mySqrt(self, x):
        # newton method
        if x == 0:
            return 0
        ans = 1
        while True:
            ans = (ans + x / ans) / 2
            if abs(ans - x / ans) < 1e-6:
                return int(ans)


s = Solution()
l = s.mySqrt(10000256644)
print(l)
l = s.mySqrt(2000000000)
print(l)
l = s.mySqrt(8)
print(l)
# 4
# 1
# 2
# 3
# 99
# 100
# 2000000000