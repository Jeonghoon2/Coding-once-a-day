from itertools import combinations


class Solution:
    def combinationSum2(self, candidates, target):

        res = []
        self.DFS(sorted(candidates), target, 0, [], res)
        return res

    def DFS(self, nums, target, idx, path, res):
        if target == 0:
            res.append(path)
        elif target < 0:
            return
        for i in range(idx, len(nums)):
            # 중복 처리
            if i > idx and nums[i] == nums[i - 1]:
                continue
            self.DFS(nums, target - nums[i], i + 1, path + [nums[i]], res)

        return res


candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
print(Solution().combinationSum2(candidates, target))
