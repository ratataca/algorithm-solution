# L 자리 수
# C 전체 문자 수

def make_secret_num(i, txt, L, isPlus):
    if i >= len(arr):
        return False

    if isPlus:
        txt += arr[i]
        if L == len(txt) and 0 < txt.count('a') + txt.count('e') + txt.count('i') + txt.count('o') + txt.count('u') < L - 1:
            print(txt)

    make_secret_num(i + 1, txt, L, True)
    make_secret_num(i + 1, txt, L, False)


L, C = [int(i) for i in input().split(" ")]
global arr
arr = [n for n in input().split(" ")]
arr = sorted(arr)

txt = ""
make_secret_num(-1, txt, L, False)
