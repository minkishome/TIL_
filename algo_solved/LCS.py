line1 = list(input())
line2 = list(input())


dict_line = dict()

for i in line1:
    if dict_line.get(i):
        dict_line[i] += 1
    else:
        dict_line[i] = 1

for i in line2:
    if dict_line.get(i):
        dict_line[i] += 1
    else:
        dict_line[i] = 1
print(dict_line)

answer = 0
for key, value in dict_line.items():
    answer += (value // 2)

print(answer)