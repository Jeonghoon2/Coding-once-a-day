# targer < 150
# 완탐 or DFS
from collections import deque


class Solution:
    def combinationSum(self, candidates, target):
        answer = []
        visit = []

        def dfs(n_sum, nums):
            # n_sum 이 0 보다 작을 경우
            if n_sum < 0:
                return
            elif n_sum > target:
                return
            # n_sun 이 target 일 경우
            elif n_sum == target:
                bool_visit = sorted(nums)
                if bool_visit not in visit:
                    visit.append(bool_visit)
                    answer.append(nums)
                return

            # dfs 돌리기
            for i in range(len(candidates)):
                dfs(n_sum + candidates[i], nums + [candidates[i]])

        dfs(0, [])
        return answer

candidates = [2,3,6,7]
target = 7
print(Solution2().combinationSum(candidates, target))
