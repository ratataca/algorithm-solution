import sys

cnt = int(sys.stdin.readline())
for i in range(cnt):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)