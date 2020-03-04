from typing import List


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
