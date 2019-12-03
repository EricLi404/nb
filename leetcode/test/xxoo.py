class xxoo(object):
    xo = [["-", "-", "-"] for _ in range(3)]
    step = 0
    s = (["A", "B"] * 5)[:9]

    def p(self):
        for aa in self.xo:
            print(aa[0], aa[1], aa[2])

    def n(self):
        value = input('| %s | input next step:' % self.s[self.step])
        sl = list(map(lambda x: int(x), value.split(",")))
        self.xo[sl[0]][sl[1]] = "x" if self.s[self.step] == "A" else "o"
        self.step += 1
        self.p()
        print("========step:%s===========" % self.step)


xoxo = xxoo()
for i in range(len(xoxo.s)):
    xoxo.n()
