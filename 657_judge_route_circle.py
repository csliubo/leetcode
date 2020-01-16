# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        count = {
            "U": 0x0,
            "D": 0x3,
            "L": 0x1,
            "R": 0x2
        }
        up_count, down_count, left_count, right_count = 0, 0, 0, 0
        ret = count[moves[0]]
        # print ret
        for ch in moves[1:]:
            ret ^= count[ch]
            # print ret
        # if count["U"] == count["D"] and count["L"] == count['R']:
        #     return True
        return ret == 3 or ret == 0


moves = "LL"
s = Solution()
print s.judgeCircle(moves)
