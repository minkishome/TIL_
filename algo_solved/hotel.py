# def solution(k, room_number):
#     answer = [0] * (k+1)
#
#     list_room = [0] * (k+1)
#
#     customer = len(room_number)
#
#     next_list = dict()
#     for num in room_number:
#         if not list_room[num]:
#             answer.append(num)
#             list_room[num] = 1
#         else:
#             while True:
#                 num += 1
#                 if not list_room[num]:
#                     answer.append(num)
#                     list_room[num] = 1
#                     break
#
#
#
#
#     return answer



def solution(k, room_number):
    answer = []
    room_info = {}
    for num in room_number:
        number = room_info.get(num, 0)
        if number:
            temp = [num]
            while 1:
                index = number
                number = room_info.get(number, 0)
                if number == 0:
                    answer.append(index)
                    room_info[index] = index + 1
                    for i in temp:
                        room_info[i] = index + 1
                    break
                temp.append(number)
        else:
            answer.append(num)
            room_info[num] = num + 1
    return answer


print(solution(10, [1,3,4,1,3,1]))
