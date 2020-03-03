from typing import List

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count_map = {}
        for num in arr:
            count_map[num] = (count_map.get(num) or 0) + 1
        limit = len(arr) // 2
        cur_count = 0
        for index, num in enumerate(sorted([v for k, v in count_map.items()], reverse=True)):
            cur_count += num
            if cur_count >= limit:
                return index + 1


s = Solution()
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
r = s.minSetSize(arr)
print(r)
arr = [1000,1000,3,7]
r = s.minSetSize(arr)
print(r)
arr = [1,9]
r = s.minSetSize(arr)
print(r)
arr = [3,3,3,3,5,5,5,2,2,7]
r = s.minSetSize(arr)
print(r)
arr = [7,7,7,7,7,7]
r = s.minSetSize(arr)
print(r)