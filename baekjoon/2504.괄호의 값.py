import sys

def cal(start):
    r = 0
    while s:
        a = s.pop()
        print("1. ", a)
        if a == "(" or a == "[":
            r += cal(a)
        elif start == "(" and a == ")":
            return 2 * max(1, r)
        elif start == "[" and a == "]":
            return 3 * max(1, r)

    # 리스트가 비었는데 최종 return 하지 못했다는 것은 괄호에 문제가 있음을 의미
    print(0)
    sys.exit()

input = sys.stdin.readline
s = list(input().rstrip())[::-1]

ans = 0
while s:
    ans += cal(s.pop())
    print(">>", ans)
print(ans)
