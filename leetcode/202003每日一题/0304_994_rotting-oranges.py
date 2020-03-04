# https://leetcode-cn.com/problems/rotting-oranges/


from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        flag = True
        cnt = 0
        tmp_g = []
        for i in grid:
            tmp_a = []
            for j in i:
                tmp_a.append(j)
            tmp_g.append(tmp_a)
        while flag:
            flag = False
            grid = []
            for i in tmp_g:
                tmp_a = []
                for j in i:
                    tmp_a.append(j)
                grid.append(tmp_a)
            # print(cnt, grid)
            # print("========")

            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j] == 2:
                        if j - 1 >= 0 and grid[i][j - 1] == 1:
                            tmp_g[i][j - 1] = 2
                            flag = True
                        if j + 1 < len(grid[i]) and grid[i][j + 1] == 1:
                            tmp_g[i][j + 1] = 2
                            flag = True
                        if i - 1 >= 0 and grid[i - 1][j] == 1:
                            tmp_g[i - 1][j] = 2
                            flag = True
                        if i + 1 < len(grid) and grid[i + 1][j] == 1:
                            tmp_g[i + 1][j] = 2
                            flag = True
                    # print(i, j, grid, flag)
            cnt = cnt + 1 if flag else cnt
        for i in grid:
            for j in i:
                if j == 1:
                    return -1
        return cnt


class Solution2:
    """
    官方解法 BFS
    """

    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        rotten = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 2}  # 腐烂集合
        fresh = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 1}  # 新鲜集合
        time = 0
        while fresh:
            if not rotten: return -1
            rotten = {(i + di, j + dj) for i, j in rotten for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)] if
                      (i + di, j + dj) in fresh}  # 即将腐烂的如果在新鲜的集合中，就将它腐烂
            fresh -= rotten  # 剔除腐烂的
            time += 1
        return time


if __name__ == '__main__':
    s = Solution()
    a = s.orangesRotting([[1, 2]])
    print(a)
