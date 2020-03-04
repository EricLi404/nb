# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        prices = prices[::-1]
        maxP = prices[0]
        maxD = max(0, prices[0] - prices[1])
        for i in range(len(prices) - 1):
            if prices[i] > maxP:
                maxP = prices[i]
            if maxP - prices[i + 1] > maxD:
                maxD = maxP - prices[i + 1]
        return maxD


if __name__ == '__main__':
    s = Solution()
    # a = s.maxProfit([2, 1, 2, 1, 0, 1, 2])
    a = s.maxProfit([7, 1, 5, 3, 6, 4])
    print(a)
