# -*- coding:utf-8 -*-
from typing import List

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution:
    def count_one(self, num):
        count = 0
        while num:
            count += num & 1
            num >>= 1
        return count

    def readBinaryWatch(self, num: int) -> List[str]:
        ret = []
        for i in range(0, 12):
            hour_count = self.count_one(i)
            if hour_count == num:
                ret.append(str(i) + ":00")
            elif hour_count < num:
                minute_count = num - hour_count
                for j in range(0, 60):
                    if self.count_one(j) == minute_count:
                        if j < 10:
                            ret.append(str(i) + ":0" + str(j))
                        else:
                            ret.append(str(i) + ":" + str(j))
        return ret
