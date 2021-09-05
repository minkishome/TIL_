N = int(input())
list_num = []

for _ in range(N):
    list_num.append(int(input()))
answer = N
for i in range(N):
    if list_num[i] == 1:
        continue

    