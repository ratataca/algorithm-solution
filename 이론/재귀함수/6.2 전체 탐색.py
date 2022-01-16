
def solution(i, m):
    if m == 0:
        return 1
    if i >= len(arr):
        return 0
    res = solution(i + 1, m) or solution(i + 1, m - arr[i])
    return res

if __name__ == '__main__':

    # 입력
    arr_len = int(input())
    global arr
    arr = [int(n) for n in input().split(" ")]

    find_len = int(input())
    find = [int(n) for n in input().split(" ")]

    # 결과
    for m in find:
        if solution(0, m):
            print("yes")
        else:
            print("no")
