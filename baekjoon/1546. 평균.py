T = int(input())
score = [int(n) for n in input().split()]
max_num = max(score)
sum = 0

for sco in score:
    sum += sco / max_num * 100

print(sum/T)