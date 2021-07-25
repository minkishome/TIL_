from math import inf
from collections import deque
import heapq

answer = inf


def solution(n, start, end, roads, traps):
    global answer

    list_roads = [[3001]*(n+1) for _ in range(n+1)] # 걸리는 시간
    list_route = [[0]*(n+1) for _ in range(n+1)] # 갈 수 잇는 정방향
    dict_route = { i : [] for i in range(1,n+1)}

    for i, j, time in roads:
        if time < list_roads[i][j]:
            list_roads[i][j] = time
            list_route[i][j] = 1
            dict_route[i].append(j)
            dict_route[j].append(i)

    list_trap = [0] * (n+1)
    for k in traps:
        list_trap[k] = 1

    distance = [0] * (n+1)

    dq = deque([]) # 도착점, 시간, 상태를 넣자
    while True:
        que = [] # 다익스트라
        heapq.heappush(que, (0, start))
        dist, now = heapq.heappop(que)
        


        break

    will_change = []

    for arrived in range(n+1):
        if list_route[start][arrived]:
            if list_trap[arrived]:
                dq.append([arrived, list_roads[start][arrived]]) # before가 0이면 역방향 1이면 정방향
                will_change.append(arrived)
            else:
                dq.append([arrived, list_roads[start][arrived]])

    for change in will_change:
        for num in dict_route[change]:
            list_route[change][num],list_route[num][change] = list_route[num][change], list_route[change][num]
            list_roads[change][num], list_roads[num][change] = list_roads[num][change], list_roads[change][num]

    will_change = []
        # TODO : trap 하나로 변경해가면서 해야한다.

    while dq:
        start, total_time = dq.popleft()
        if start == end:
            if total_time < answer:
                answer = total_time
                continue

        for arrived in range(n+1):
            if list_route[start][arrived]:
                new_time = total_time + list_roads[start][arrived]
                if new_time > answer:
                    continue

                dq.append([arrived, new_time])
                if list_trap[arrived]:  # before가 0이면 역방향 1이면 정방향
                    will_change.append(arrived)

        for change in will_change:
            for num in dict_route[change]:
                list_route[change][num], list_route[num][change] = list_route[num][change], list_route[change][num]
                list_roads[change][num], list_roads[num][change] = list_roads[num][change], list_roads[change][num]

        will_change = []





    return answer

print(solution(4,	1,	4,	[[1, 2, 1], [3, 2, 1], [2, 4, 1]],	[2, 3]))
