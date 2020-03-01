# 7，最大连续子数组和
#
# 题目形式：给定一个数组，求其最大连续子数组的和。例如：arr = [1,5,-10,2,5,-3,2,6,-3,1].  输出为：12。对应的连续子数组为 [2,5,-3,2,6]。
# 题目难度：中等。
# 出现概率：约15%。这道题目也是一道动态规划的祖传范例。同学，你的这个两重循环写的确实很6，但是我们不能认为你的这道题目做对了！


def f(arr):
    i, j = 0, len(arr) - 1
    ms = sum(arr)
    while i < j:
        if arr[i] < arr[j]:
            i += 1
        else:
            j -= 1
        ms = max(ms, sum(arr[i:j + 1]))
    return ms


def max_sub_array(arr):
    """
    博文中的写法
    :param arr:
    :return:
    """
    n = len(arr)
    maxi,maxall = arr[0],arr[0]
    for i in range(1,n):
        maxi = max(arr[i],maxi + arr[i])
        maxall = max(maxall,maxi)
    return(maxall)

if __name__ == '__main__':
    c = f([1, 5, -10, 2, 5, -3, 2, 6, -3, 1])
    print(c)
