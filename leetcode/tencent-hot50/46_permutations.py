# https://leetcode-cn.com/problems/permutations/

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(path, size, done, depth, res):
            if depth == size:
                res.append(path[:])
                return
            for i in nums:
                if i not in done:
                    done[i] = True
                    path.append(i)
                    dfs(path, size, done, depth + 1, res)
                    del done[i]
                    path.pop()

        path, size, done, depth, res, = [], len(nums), {}, 0, []
        dfs(path, size, done, depth, res)
        return res


if __name__ == '__main__':
    s = Solution()
    a = s.permute([1,2,3])
    print(a)
