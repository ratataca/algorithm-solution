# participant : 참여한 선수들의 이름이 담긴 배열
# completion : 완주한 선수들의 이름이 담긴 배열

# 문제) 완주하지 못한 선수의 이름을 return

from collections import defaultdict


def solution(participant, completion):
    # participant 관련 counter 딕션너리 정의
    counter = defaultdict(int)

    for p in participant:
        counter[p] += 1

    # completion 선수들을 조회하면서 counter 카운터 차감
    for p in completion:
        counter[p] -= 1

    answerd = [str(k) for k, v in counter.items() if v == 1]
    return answerd[0]