def solution(seconds : int):
    dp = [0] * (seconds + 1)

    snack = [(300, 10), (130, 30), (120, 20), (20, 30)]


    total_snack = 0

    while 1:
        for cost, total in snack:
            num1, num2 = seconds // cost, seconds % cost
            if num1 == 0:
                continue
            elif num1 > total:
                seconds -= cost*total
                continue

            elif num2 == 0:
                total_snack += num1
                return total_snack
            else:
                seconds = num2
                total_snack += num1
        else:
            break
    return total_snack
    # for cost, total_snank in snack:



solution(450)