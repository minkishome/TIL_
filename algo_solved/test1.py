from string import ascii_uppercase


def solution(name_list):
    alpha_list = list(ascii_uppercase)
    answer = []
    name_dict = dict()
    for name in name_list:
        if name_dict.get(name):
            count = name_dict.get(name)

            new_name = name + alpha_list[count]
            answer.append(new_name)
            name_dict[name] = count + 1
        else:
            name_dict[name] = 1
            new_name = name + 'A'
            answer.append(new_name)
    
    return answer

solution(["김비바", "김비바", "이비바", "김토스", "이비바", "김비바"])