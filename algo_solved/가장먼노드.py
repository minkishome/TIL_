def solution(n, edge):
    answer = 0

    node = dict()
    for key, value in edge:
        if not node.get(key):
            node[key] = [value]
        else:
            node[key].append(value)

    print(node)

    stack = node[1]
    stack_dict = dict()
    visited = [0] * (n+1)
    num = 1
    while stack:
        stack2 = []
        for num in stack:
            if not visited[num]:
                if node.get(num):
                    stack2.extend(node.get(num))
            visited[num] = 1
        if stack2:
            num += 1
            stack_dict[num] = stack2
            stack = stack2
        else:
            break
    print(stack_dict[num])

    return answer


solution(6, 	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])