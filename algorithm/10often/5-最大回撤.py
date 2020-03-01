# 题目形式：有一个数组，求其中两个数x,y，满足x的索引小于y的索引，使得 x-y 最大。例如 arr = [3,7,2,6,4,1,9,8,5]， 最大回撤是6，对应的x=7,y=1。
# 题目难度：中等。
# 出现概率：约20%。这道题目可能以买卖股票的最佳时机，或者最大抬升等各种形式出现，这也是一道动态规划的史诗级范例。呦呵，又整上两重循环了，这循环写的很可以啊。

def maxr(arr):
    """
    我写的，不知道有没有啥问题
    :param arr:
    :return:
    """
    if len(arr) < 2:
        return 0
    mx = arr[0]
    mr = mx - arr[1]
    for i in range(1, len(arr)):
        y = arr[i]
        mr = max(mr, mx - y)
        mx = max(mx, y)
    return mr


def max_drawdown(arr):
    """
    官方写法
    :param arr:
    :return:
    """
    assert len(arr) > 2, "len(arr) should > 2!"
    x, y = arr[0:2]
    xmax = x
    maxdiff = x - y

    for i in range(2, len(arr)):
        if arr[i - 1] > xmax:
            xmax = arr[i - 1]
        if xmax - arr[i] > maxdiff:
            maxdiff = xmax - arr[i]
            x, y = xmax, arr[i]

    print("x=", x, ",y=", y)
    return (maxdiff)


if __name__ == '__main__':
    print(maxr([3, 7, 2, 6, 4, 1, 9, 8, 5]))
