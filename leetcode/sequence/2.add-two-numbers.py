class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        v = self.gf(l1) + self.gf(l2)
        ll = ListNode(str(v)[::-1][0])
        t = ll
        for i in str(v)[::-1][1:]:
            t.next = ListNode(i)
            t = t.next
        return ll

    def gf(self, l: ListNode):
        s = 0
        c = 1
        while l.next:
            s += l.val * c
            c *= 10
            l = l.next
        s += l.val * c
        return s


def ii(ll):
    l = ListNode(ll[0])
    t = l
    for i in ll[1:]:
        print(i)
        t.next = ListNode(i)
        t = t.next
    return l


def p(lll):
    print("=====")
    while lll.next:
        print(lll.val)
        lll = lll.next
    print(lll.val)


if __name__ == "__main__":
    ll1 = [2, 4, 3]
    ll2 = [5, 6, 4]
    p(ii(ll1))
    # ss = Solution()
