# 不使用额外辅助，将一个栈逆序


from typing import List


# 原理： 使用程序调用栈记录信息，反转栈
def gb(stack: List):
    a = stack.pop()
    if not stack:
        return a
    else:
        b = gb(stack)
        stack.append(a)
        return b


def rv(stack: List):
    if not stack:
        return
    else:
        b = gb(stack)
        rv(stack)
        stack.append(b)
        return


if __name__ == '__main__':
    s = [1, 2, 3, 4, 5]
    rv(s)
    print(s)
