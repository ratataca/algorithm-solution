def solution(answers):
    correct = {1: 0, 2: 0, 3: 0, }  # idx : 사람, 값 승률

    person = [[1, 2, 3, 4, 5],
              [2, 1, 2, 3, 2, 4, 2, 5],
              [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    for i in range(3):
        for an in range(len(answers)):
            if (person[i][an % len(person[i])] == answers[an]):
                correct[i + 1] = correct[i + 1] + 1

    ranking = ranking = sorted(correct.items(), key=lambda x: x[1], reverse=True)

    ck = 0
    tmp_value = None

    for k, v in ranking:
        if tmp_value == None and v == 0:
            return [0]

        if tmp_value != None and tmp_value > v:
            break

        if tmp_value != None and tmp_value == v:
            ck += 1
        tmp_value = v

    answer = []
    if ck == 0:
        answer.append(ranking[0][0])
    elif ck == 1:
        answer.extend([ranking[0][0], ranking[1][0]])
    else:
        answer.extend([ranking[0][0], ranking[1][0], ranking[2][0]])

    return answer