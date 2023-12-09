n = int(input())

nums = list(map(int, input().split()))

operations = list(map(int, input().split()))

min_ans = int(1e9)
max_ans = int(1e9) * -1


def dfs(idx, o):
    global max_ans
    global min_ans

    if idx == len(nums):
        max_ans = max(max_ans, o)
        min_ans = min(min_ans, o)
        return

    for i in range(len(operations)):
        cur_o = o
        if operations[i] == 0:
            continue
        operations[i] -= 1
        if i == 0:
            cur_o += nums[idx]
        elif i == 1:
            cur_o -= nums[idx]
        elif i == 2:
            cur_o *= nums[idx]
        else:
            cur_o = int(cur_o / nums[idx])

        dfs(idx + 1, cur_o)

        operations[i] += 1


dfs(1, nums[0])

print(max_ans)
print(min_ans)
