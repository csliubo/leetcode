# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
        i = 0
        ret = []
        while i < numRows:
            j = 0
            arr = []
            # print arr, arr.__len__()
            while j <= i:
                # print i, j
                if j == 0 or j == i:
                    # arr[j] = 1
                    arr.insert(j, 1)
                else:
                    arr.insert(j, ret[i - 1][j - 1] + ret[i - 1][j])
                j += 1
            ret.append(arr)
            i += 1
        return ret


s = Solution()
# for i in range(1, 100):
#     print s.generate(i)
print s.generate(100)