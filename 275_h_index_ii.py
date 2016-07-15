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
        if citations[citations.__len__() - 1] == 0:
            return 0
        for i in xrange(citations.__len__() - 1, -1, -1):
            pos = citations.__len__() - i
            if citations[i] >= pos:
                pass
            else:
                return pos - 1
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

citations = [1,2,3,4,10]
print s.hIndex(citations)