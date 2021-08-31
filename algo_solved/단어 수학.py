import operator

N = int(input())

words = []
max_len = 0
for _ in range(N):
    ls = list(input())
    if max_len < len(ls):
        max_len = len(ls)
    ls.reverse()
    words.append(ls)

dict_alpa = dict()

for word in words:
    for i in range(len(word)):
        if not dict_alpa.get(word[i]):
            dict_alpa[word[i]] = 10 ** i
        else:
            dict_alpa[word[i]] += 10 ** i


lsls = sorted(dict_alpa.items(), key=operator.itemgetter(1), reverse=True)
num = 9
answer = 0
for alph_num in lsls:
    answer += num * alph_num[1]
    num -= 1
print(answer)
# for i in range(N):
#     words[i] = words[i] + (max_len - len(words[i])) * [0]
#     words[i].reverse()
# list_num = [ i for i in range(9,-1, -1)]
# visited = [0] * 10
#
#
#
# string_num = dict()
#
# for j in range(max_len):
#     for i in range(N):
#         if words[i][j]:
#             if not string_num.get(words[i][j]):
#                 for num in list_num:
#                     if not visited[num]:
#                         string_num[words[i][j]] = num
#                         visited[num] = 1
#                         break
#         else:
#             words[i][j] = str(words[i][j])
#
#
# for i in range(N):
#     for j in range(max_len):
#         if words[i][j] != '0':
#             words[i][j] = str(string_num[words[i][j]])
#     words[i] = int(''.join(words[i]))
#
# print(list_num)
# print(string_num)
# print(sum(words))