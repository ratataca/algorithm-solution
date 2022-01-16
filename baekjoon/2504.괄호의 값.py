#
#
# def solution(i, all, find , num):
#     if i == len(rep):
#         return
#
#     if find == ")":
#         num += 2
#
#     if find == "]":
#         num += 3
#
#     if rep[i] == "(":
#         solution(i+1, all, ")", num)
#
#     elif rep[i] == "[":
#         solution(i+1, all, "]", num)
#
#
#
# num = 0
# global rep
# rep = [s for s in input()]
# print(rep)
# all = 0
#
# solution(0, all, rep[0], num)
# print(num)


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
