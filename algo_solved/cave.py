from collections import defaultdict, deque


# def solution(n, path, order):
#     answer = True
#     dict_sort = defaultdict(list)
#     dict_path = defaultdict(list)
#     dict_order = defaultdict(int)   # 가기 위한 조건 반대
#     dict_order2 = defaultdict(int) # 가기 위한 조건
#     visited_sort = [0]*n
#
#     for a, b in path:
#         dict_sort[a].append(b)
#         dict_sort[b].append(a)
#
#     stack = [0]
#     visited_sort[0] = 1
#     for k in stack:
#         if dict_sort[k]:
#             for num in dict_sort[k]:
#                 if not visited_sort[num]:
#                     dict_path[k].append(num)
#                     visited_sort[num] = 1
#                     stack.append(num)
#     # 정렬 과정
#
#     for num1, num2 in order:
#         dict_order[num1] = num2
#         dict_order2[num2] = num1
#
#     visited = [0] * n
#     check = []
#     que = deque([0])
#     while que:
#
#         q = que.popleft()
#         if dict_order2[q] and not visited[dict_order2[q]]:
#             check.append(dict_order2[q])
#             continue
#
#         visited[q] = 1
#         for num in dict_path[q]:
#             if not visited[num]:
#                 que.append(num)
#
#
#         if q in check:
#             que.append(dict_order[q])
#
#
#     return n == sum(visited)
#

def solution(n, path, order):
    answer = True
    # dict_sort = defaultdict(list)
    # dict_path = defaultdict(list)
    # dict_order = defaultdict(int)   # 가기 위한 조건 반대
    # dict_order2 = defaultdict(int) # 가기 위한 조건
    ls_sort = [ [] for _ in range(n) ]
    ls_path = [ [] for _ in range(n) ]
    ls_order = [0] * n
    ls_order2 = [0] * n

    visited_sort = [0]*n

    for a, b in path:
        ls_sort[a].append(b)
        ls_sort[b].append(a)

    stack = [0]
    visited_sort[0] = 1
    for k in stack:
        if ls_sort[k]:
            for num in ls_sort[k]:
                if not visited_sort[num]:
                    ls_path[k].append(num)
                    visited_sort[num] = 1
                    stack.append(num)
    # 정렬 과정

    for num1, num2 in order:
        ls_order[num1] = num2
        ls_order2[num2] = num1

    visited = [0] * n
    check = []
    que = deque([0])
    while que:

        q = que.popleft()
        if ls_order2[q] and not visited[ls_order2[q]]:
            check.append(ls_order2[q])
            continue

        visited[q] = 1
        for num in ls_path[q]:
            if not visited[num]:
                que.append(num)


        if q in check:
            que.append(ls_order[q])


    return n == sum(visited)


print(solution(9,	[[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]]	,[[4,1],[8,7],[6,5]]			))

