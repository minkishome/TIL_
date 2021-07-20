def solution(k, room_number):
    answer = [0] * (k+1)

    list_room = [0] * (k+1)

    customer = len(room_number)

    next_list = dict()
    for num in room_number:
        if not list_room[num]:
            answer.append(num)
            list_room[num] = 1
        else:
            while True:
                num += 1
                if not list_room[num]:
                    answer.append(num)
                    list_room[num] = 1
                    break




    return answer




print(solution(10, [1,3,4,1,3,1]))