from collections import defaultdict


def solution(clothes):
    answer = 1
    my_clothe = defaultdict(int)

    for v, k in clothes:
        my_clothe[k] += 1

    for k, v in my_clothe.items():
        my_clothe[k] += 1
        answer *= my_clothe[k]

    return answer - 1