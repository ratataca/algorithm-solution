def solution(lottos, win_nums):
    answer = []
    correct = 0
    unknown = 0

    for i in lottos:
        if i in win_nums:
            correct += 1
        if i == 0:
            unknown += 1

    answer.append(7 - (correct + unknown))
    answer.append(7 - correct)

    for i in range(len(answer)):
        if answer[i] > 6:
            answer[i] = 6

    return answer

