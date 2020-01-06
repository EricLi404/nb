# -*- coding: utf-8 -*-
# @Author:<leiflyy@outlook.com>
class Solution:
    # def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
    def shiftGrid(self, grid, k):
        a = len(grid)
        b = len(grid[0])
        c = a * b
        real_k = k % c
        grid2 = list(map(lambda x:x*1, grid)
        for i in range(c):
            print(grid,grid2)
            print(i,(int(i / b),i % b),(int((i - real_k) / b) % a,(i + real_k) % b),grid2[int((i - real_k) / b) % a ][(i + real_k) % b])
            grid[int(i / b)][i % b] = grid2[int((i + real_k) / b) % a ][(i + real_k) % b]
        return grid


c = Solution()

#  grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
grid = [[1,2,3],[4,5,6],[7,8,9]]
#  grid = [[1]]
k = 1

o = c.shiftGrid(grid, k)
print(o)
