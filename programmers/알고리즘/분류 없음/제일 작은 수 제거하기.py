def solution(arr):
    del arr[arr.index(min(arr))]
    if len(arr) > 0:
        return arr
    return [-1]