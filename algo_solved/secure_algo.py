T = int(input())
"""
1문 -> 2문 평문 -> 암호문
"""
for _ in range(T):
    n = int(input())
    first_secure = list(input().split())
    second_secure = list(input().split())
    secure = list(input().split())
    first_dict = dict()
    second_dict = dict()
    for i in range(n):
        first_dict[first_secure[i]] = i
        second_dict[second_secure[i]] = i
    # print(first_dict, second_dict)

    list_order = []

    for word in first_secure:
        list_order.append((first_dict[word], second_dict[word]))
    # print(list_order)

    answer = ['word']*n
    # print(secure)
    for num2, num1 in list_order:
        answer[num2] = secure[num1]
    print(' '.join(answer)

    # print(first_secure, second_secure)
