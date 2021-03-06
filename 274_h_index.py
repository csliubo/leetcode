# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        citations = sorted(citations, reverse=True)
        if citations[0] == 0:
            return 0
        for i in xrange(0, citations.__len__()):
            if citations[i] >= i + 1:
                pass
            else:
                return i
        return citations.__len__()


citations = [1, 2]
s = Solution()
print s.hIndex(citations)

citations = []
print s.hIndex(citations)

citations = [0]
print s.hIndex(citations)

citations = [100]
print s.hIndex(citations)

citations = [1, 2, 3, 4, 10]
print s.hIndex(citations)
