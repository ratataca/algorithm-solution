cnt = 0
target = int(input())
num = target

while True:
    # 각 자리수 더하기
    ten, select_num1 = num // 10, num % 10

    # 주어진 수의 가장 오른쪽 자리와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙임
    select_num2 = (ten + select_num1) % 10
    num = select_num1 * 10 + select_num2
    cnt += 1

    # 원래 수로 돌아오면 CNT를 반환하라.
    if target == num:
        break

print(cnt)
