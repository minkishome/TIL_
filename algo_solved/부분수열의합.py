def dfs(number):
    global visited, answer, S, N
    if number == S:
        answer += 1
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = 1
                number += ls_num[i]
                dfs(number)

                visited[i] = 0
                number -= ls_num[i]

def dfs2(idx, sum_number):
    global visited, answer, S, N, ls_num
    if idx >= N:
        return
    sum_number += ls_num[idx]
    if sum_number == S:
        answer += 1
    dfs2(idx+1, sum_number)
    dfs2(idx+1, sum_number-ls_num[idx])


N, S = map(int, input().split())

ls_num = list(map(int, input().split()))
ls_num.sort()
visited = [0] * N
answer = 0

dfs2(0, 0)
print(answer)

