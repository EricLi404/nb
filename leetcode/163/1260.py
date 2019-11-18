# -*- coding: utf-8 -*-
# @Author:<leiflyy@outlook.com>
class Solution:
    # def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
    def shiftGrid(self, grid, k):
        real_k = k % (len(grid) + len(grid[0]))
        one_line_grid = []
        for a_l in grid:
            one_line_grid += a_l
        o = [[]]
        for i in range(len(one_line_grid)):
            #  o.append(one_line_grid[(i + real_k) % len(one_line_grid)])
        return o


c = Solution()

grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#  grid = [[1]]
k = 10

o = c.shiftGrid(grid, k)
print(o)
