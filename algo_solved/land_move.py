# from collections import deque
# from math import inf
#
# def isxy(x,y,n):
#     return 0 <= x < n and 0 <= y < n
#
# def solution(land, height):
#     answer = 0
#     n = len(land)
#
#     visited = [[inf] * n for _ in range(n)]
#     visited[0][0] = 0
#     xy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
#
#     for k in visited:
#         print(k)
#
#     que = deque([])
#     que.append((0, 0, 0))
#
#     while que:
#         x, y, price = que.popleft()
#         for dx, dy in xy:
#             new_x, new_y = x+dx, y+dy
#             if isxy(new_x, new_y, n) and visited[new_x][new_y] > price:
#                 if abs(land[new_x][new_y] - land[x][y]) <= height:
#                     que.append((new_x, new_y))
#                     visited[new_x][new_y] = 0
#                 else:
#                     if land[x][y] + abs(land[new_x][new_y] - land[x][y]) < visited[new_x][new_y]:
#                         que.append((new_x, new_y))
#                         visited[new_x][new_y] = abs(land[new_x][new_y] - land[x][y])
#         for k in visited:
#             print(k)
#     for k in visited:
#         print(k)
#     for k in visited:
#         answer += sum(k)

import heapq

def solution(land, height):
    n = len(land)
    visited = [[0]*n for _ in range(n)]


    xy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    que = [(0, 0, 0)]

    max_count = n*n
    visit = 0
    answer = 0

    while visit < max_count:
        cost, x, y = heapq.heappop(que)
        if visited[x][y]:
            continue
        visited[x][y] = 1
        visit += 1
        answer += cost

        now_height = land[x][y]

        for dx, dy in xy:
            if 0 <= x+dx < n and 0 <= y+dy < n:
                new_height = land[x+dx][y+dy]
                if abs(new_height - now_height) <= height:
                    heapq.heappush(que, (0, x+dx, y+dy))
                else:
                    heapq.heappush(que, (abs(new_height-now_height), x + dx, y + dy))


    return answer






print(solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]], 3))