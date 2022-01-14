def solution(arr):
    answer = []
    txt = ""
    for a in arr:
        if txt != a:
            answer.append(a)
        txt = a
    return answer