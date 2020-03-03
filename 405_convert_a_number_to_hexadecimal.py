# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution:
    hex_map = {
        0: '0',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        10: 'a',
        11: 'b',
        12: 'c',
        13: 'd',
        14: 'e',
        15: 'f'
    }

    def intToBin32(self, i):
        print(((1 << 32) - 1) & i)
        return (bin(((1 << 32) - 1) & i)[2:]).zfill(32)

    def toHex(self, num: int) -> str:
        ret = ''
        if num < 0:
            num = (((1 << 32) - 1) & num)
        while num:
            ret = self.hex_map.get(num & 0xf) + ret
            num >>= 4
        return ret


s = Solution()
print(s.intToBin32(-1))
print(s.intToBin32(1))
