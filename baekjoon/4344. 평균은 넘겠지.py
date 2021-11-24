T = int(input())

while T:
    score = [int(n) for n in input().split()]
    score_len = score.pop(0)
    score_avg = sum(score) / score_len

    cnt = 0
    for s in score:
        if score_avg < s:
            cnt += 1

    print("{:.3f}%".format(cnt / score_len * 100))
    T -= 1