class Solution(object):

    def maxConsecutiveAnswers(self, answerKey, k):

        result = 0
        max_count = 0
        count = dict()

        for i in range(len(answerKey)):

            if answerKey[i] not in count:
                count[answerKey[i]] = 1
            else:
                count[answerKey[i]] = count.get(answerKey[i]) + 1

            max_count = max(max_count, count.get(answerKey[i]))
            if result - max_count >= k:
                count[answerKey[i-result]] = count.get(answerKey[i-result]) - 1
            else:
                result += 1
        return result


print(Solution().maxConsecutiveAnswers("TTFTTFTT", 1))
