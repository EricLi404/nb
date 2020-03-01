# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/

# 给定一个字符串，找出没有重复字符的最长的子串。例如输入“abcbefgf”，答案是 “cbefg”


# 边界问题！！！
def f(s):
    i, j = 0, 0
    l = list(s)
    l.append(" ")
    m = []
    while j < len(s):
        j += 1
        if len(l[i:j]) >= len(m):
            m = l[i:j]
        try:
            i += l[i:j].index(l[j]) + 1
        except:
            pass
        print((i, j), m, l[j], l[i:j])

    return "".join(m)


def f1(s):
    d = {}
    i, j = 0, 0
    sl = []
    while j < len(s):
        if s[j] in d:
            i = max(d[s[j]] + 1, i)
        d[s[j]] = j
        if j - i + 1 > len(sl):
            sl = s[i:j + 1]
        j += 1
    return sl


def f2(s):
    m, i, j = 0, 0, 0
    l = list(s)
    l.append(" ")

    while j < len(s):
        j += 1
        m = max(j - i, m)
        try:
            i += l[i:j].index(l[j]) + 1
        except:
            pass
    return m


if __name__ == '__main__':
    c = f1("abcabcbb")
    # c = f1("abcbefgf")
    print(c)
