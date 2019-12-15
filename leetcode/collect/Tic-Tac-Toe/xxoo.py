import os


class xxoo(object):
    xo = [["-", "-", "-"] for _ in range(3)]
    step = 0
    s = (["A", "B"] * 5)[:9]
    A = []
    B = []

    def judge(self, m):
        s = [
            [[0, 0], [0, 1], [0, 2]],
            [[1, 0], [1, 1], [1, 2]],
            [[2, 0], [2, 1], [2, 2]],
            [[0, 0], [1, 0], [2, 0]],
            [[0, 1], [1, 1], [2, 1]],
            [[0, 2], [1, 2], [2, 2]],
            [[0, 0], [1, 1], [2, 2]],
            [[0, 2], [1, 1], [2, 0]],
        ]
        flags = 0
        if len(m) >= 3:
            for i in s:
                flags = 0
                for j in m:
                    if j in i:
                        flags += 1
                if flags == 3:
                    return True
        return False

    def p(self):
        for aa in self.xo:
            print(aa[0], aa[1], aa[2])

    def n(self):
        value = input('| %s | input next step:' % self.s[self.step])
        try:
            sl = list(map(lambda x: int(x), value.split(",")))
        except:
            print("wrong params")
            return
        if self.xo[sl[0]][sl[1]] != "-":
            print("wrong position")
        else:
            self.xo[sl[0]][sl[1]] = "x" if self.s[self.step] == "A" else "o"
            if self.step % 2 == 0:
                self.A.append(sl)
                fl = self.judge(self.A)
                if fl:
                    print("A win !!!")
                    exit(0)
            else:
                self.B.append(sl)
                fl = self.judge(self.A)
                if fl:
                    print("B win !!!")
                    exit(0)
            self.step += 1
            self.p()
            print("========step:%s===========" % self.step)


if __name__ == "__main__":
    xoxo = xxoo()
    for i in range(len(xoxo.s)):
        xoxo.n()
