# https://www.acmicpc.net/problem/10816
from collections import defaultdict

N = int(input())
cards = [int(n) for n in input().split()]

M = int(input())

checks = defaultdict()
for key in [int(n) for n in input().split()]:
    checks[key] = 0

for card in cards:
    if card in checks:
        checks[card] = checks[card] + 1
    

print(' '.join([str(s) for s in checks.values()]))


