class Solution:
    # TODO
    # def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
    def xorQueries(self, arr, queries):
        r = []
        for c in queries:
            s = 0
            if c[0] == c[1]:
                r.append(arr[c[0] ^ arr[c[1]]])
                continue
            cc = c[0]
            while cc <= c[1]:
                print(cc, c[1])
                if cc < c[1] and arr[cc] == arr[cc + 1]:
                    cc += 1
                    print("ccc ", s)
                    continue
                s ^= arr[cc]
                cc += 1
                print("nnn ", s)
            print("====")
            r.append(s)
        return r


if __name__ == "__main__":
    ss = Solution()
    arr = [4, 2, 3, 5, 5]
    queries = [[2, 2], [4, 4], [0, 4], [4, 4]]
    r = ss.xorQueries(arr, queries)
    print(r)
