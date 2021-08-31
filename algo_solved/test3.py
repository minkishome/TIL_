def solution(csv_string, keyword):

    team_list = []
    node = dict()
    new_csv = csv_string.split('\n')
    list_info = []
    for i in range(1, len(new_csv)):
        list_info.append(new_csv[i].split(','))

    for info in list_info:
        team_list.append(info[1])
        if info[2]:
            if node.get(list_info[int(info[2])-1][1]):
                node[list_info[int(info[2])-1][1]].append(info[1])
            else:
                node[list_info[int(info[2])-1][1]] = [info[1]]
        else:
            node[info[1]] = []

    answer = []
    for team in team_list:
        if keyword in team:
            answer.append(team)


    for team in answer:

        if node.get(team):
            answer.extend(node[team])

    answer = list(set(answer))
    if not answer:
        return -1
    people = 0
    for name in answer:
        for info in list_info:
            if name == info[1]:
                people += int(info[3])


    return people

csv = "조직 ID,조직명,상위 조직 ID,소속 팀원 수\n1,토스팀,,1\n2,인터널 트라이브,1,1\n3,인터널 매니저 팀,2,7\n4,비바 플랫폼 팀,2,14\n5,아웃터널 트라이브,1,2\n6,가이드 팀,5,4\n7,피트아웃 사일로,5,11"
solution(csv, "아웃")