# https://leetcode-cn.com/problems/climbing-stairs/

# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？


class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return b


if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(5))
