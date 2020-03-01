# https://leetcode-cn.com/problems/lru-cache/

class LRUCache:

    def __init__(self, capacity: int):
        self.c = capacity
        self.l = []
        self.d = {}

    def get(self, key: int) -> int:
        if key in self.d:
            self.l.pop(self.l.index(key))
            self.l.append(key)
            return self.d[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.l.pop(self.l.index(key))
            self.l.append(key)
            self.d[key] = value
        else:
            self.d[key] = value
            self.l.append(key)
            if len(self.l) > self.c:
                del (self.d[self.l.pop(0)])
