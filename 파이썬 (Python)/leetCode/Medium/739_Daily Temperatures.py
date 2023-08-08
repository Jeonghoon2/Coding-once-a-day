class Solution:
    def dailyTemperatures(self, temperatures):
        answer = [0] * len(temperatures)
        t = []
        for i, k in enumerate(temperatures):
            while t and t[-1][1] < k:
                p_day, _ = t.pop()
                answer[p_day] = i - p_day
            t.append((i, k))

        return answer


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(Solution().dailyTemperatures(temperatures))
