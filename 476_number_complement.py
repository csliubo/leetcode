# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution(object):
    TWO_POWERS = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144,
                  524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456,
                  536870912, 1073741824, 2147483648]

    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        for two_power in self.TWO_POWERS:
            if num < two_power:
                return two_power - 1 - num
        return 0


s = Solution()
print s.findComplement(7)
print s.findComplement(5)
# ret = []
# for i in range(0, 32):
#     ret.append(str(pow(2, i)))
# print ",".join(ret)
