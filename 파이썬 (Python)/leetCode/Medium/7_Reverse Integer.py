import collections


class Solution:
    def reverse(self, x: int) -> int:

        # 음양 구하기
        flag = -1
        if x > 0:
            flag = 1

        x = list(str(x))
        s = len(x)
        tmp = collections.deque()

        for _ in range(s):
            cur_c = x.pop()
            if cur_c == '-':
                tmp.appendleft(cur_c)
                continue
            tmp.append(cur_c)

        x = ''
        for i in tmp:
            x += i

        return int(x) if (2 ** 31)*-1 <= int(x) <= 2 ** 31 else 0


print(Solution().reverse(x=-123))
