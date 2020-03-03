from typing import List

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m, n = len(mat), len(mat[0])
        z = []
        for i in range(0, m):
            count = 0
            for num in mat[i]:
                if num == 0:
                    break
                count += num
            z.append((count, i))

        return [num[1] for num in sorted(z, key=lambda x: (x[0], x[1]))][:k]


s = Solution()
mat = [[1, 1, 0, 0, 0],
       [1, 1, 1, 1, 0],
       [1, 0, 0, 0, 0],
       [1, 1, 0, 0, 0],
       [1, 1, 1, 1, 1]]
k = 3

r = s.kWeakestRows(mat, k)
print(r)
mat = [[1, 0, 0, 0],
       [1, 1, 1, 1],
       [1, 0, 0, 0],
       [1, 0, 0, 0]]
k = 2
r = s.kWeakestRows(mat, k)
print(r)
