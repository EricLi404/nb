# -*- coding: utf-8 -*-
# @Author:<leiflyy@outlook.com>
class Solution:
    # def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
    def shiftGrid(self, grid, k):
        a = len(grid)
        b = len(grid[0])
        c = a * b
        real_k = k % c
        if real_k == 0:
            return grid
        one_line_grid = []
        for a_l in grid:
            one_line_grid += a_l
        for i in range(c):
            grid[int(i / b)][i % b] = one_line_grid[(i - real_k) % c]
        return grid


c = Solution()

grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
#  grid = [[1]]
k = 2

o = c.shiftGrid(grid, k)
print(o)
