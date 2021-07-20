from math import inf
from collections import deque

answer = inf

def solution(n, start, end, roads, traps):
    global answer

    list_roads = [[3001]*(n+1) for _ in range(n+1)] # 걸리는 시간
    list_route = [[]*(n+1) for _ in range(n+1)] # 갈 수 잇는 정방향
    reverse_list_route = [[]*(n+1) for _ in range(n+1)] # 갈수있는 역방향
    for i, j, time in roads:
        if time < list_roads[i][j]:
            list_roads[i][j] = time
            list_route[i].append(j)

        if time < list_roads[j][i]:
            list_roads[j][i] = time
            reverse_list_route[j].append(i)
    # deque 넣을 꺼 -> (x,y,total_time)

    list_trap = [0] * (n+1)
    for k in traps:
        list_trap[k] = 1

    dq = deque([]) # 도착점, 시간, 상태를 넣자
    for arrived in list_route[start]:
        if list_trap[arrived]:
            dq.append([arrived, list_roads[start][arrived], 1, 0]) # before가 0이면 역방향 1이면 정방향
        else:
            dq.append([arrived, list_roads[start][arrived], 1, 1])
    # TODO : trap위치만 바뀐다.
    
    while dq:
        start, total_time, direction, true_false = dq.popleft()
        if start == end:
            if total_time < answer:
                answer = total_time
                continue

        if direction:

            if true_false:
                list_q = list_route
                dir = 1
            else:
                list_q = reverse_list_route
                dir = 0

            if list_q[start]:
                for new_start in list_q[start]:
                    new_time = total_time + list_roads[start][new_start]
                    if new_time < answer:
                        if list_trap[new_start]:
                            dq.append([new_start, new_time, dir, 0])
                        else:
                            dq.append([new_start, new_time, dir, 1])
        else:
            if true_false:
                list_q = reverse_list_route
                dir = 0
            else:
                list_q = list_route
                dir = 1

            if list_q[start]:
                for new_start in list_q[start]:
                    new_time = total_time + list_roads[start][new_start]
                    if new_time < answer:
                        if list_trap[new_start]:
                            dq.append([new_start, new_time, dir, 0])
                        else:
                            dq.append([new_start, new_time, dir, 1])


        #
        # if status: # 정방향
        #     if before:
        #         list_q = list_route
        #     else:
        #         list_q = reverse_list_route
        #     if list_q[start]:
        #         for new_start in list_q[start]:
        #             new_time = total_time + list_roads[start][new_start]
        #             if new_time < answer:
        #                 if list_trap[new_start]:
        #                     dq.append([new_start, new_time, 0, 1])
        #                 else:
        #                     dq.append([new_start, new_time, 1, 1])
        #
        # else:
        #     if before:
        #         list_q = reverse_list_route
        #     else:
        #         list_q = list_route
        #     if list_q[start]:
        #         if reverse_list_route[start]:
        #             for new_start in reverse_list_route[start]:
        #                 new_time = total_time + list_roads[start][new_start]
        #                 if new_time < answer:
        #                     if list_trap[new_start]:
        #                         dq.append([new_start, new_time, 0, 0])
        #                     else:
        #                         dq.append([new_start, new_time, 1, 0])




    return answer

print(solution(4,	1,	4,	[[1, 2, 1], [3, 2, 1], [2, 4, 1]],	[2, 3]))
