# from collections import defaultdict
#
# n = int(input())
# data = [int(i) for i in input().split()]
#
#
# min_location = defaultdict(int)
#
# for i in range(len(data)):
#     for j in range(len(data)):
#         min_location[data[i]] += abs(data[i] - data[j])
#
# min_location = sorted(min_location.items(), key= lambda x : x[1])
# print(min_location[0][0])
#


def test(a):
    n = len(a)
    for i in range(n // 2):
        a[i], a[n - i - 1] = a[n - i - 1], a[i]

a = [2, 5, 1, 3, 9, 6, 7]
test(a)
print(a)

# n = 5
# sum = 0
# for i in range(1, n+1): # 1,2, 3, 4, 5
#     if i == 3:
#         continue
#     else:
#         sum += i
# print(sum)


# def test(n):
#     if n > 0:
#         return n * test(n-1)
#     else:
#         return 1
#
# print(test(3))



cnt = 0
for i in range(1, 5):
    if i == 3:
        break
    for j in range(1, 5):
        cnt += 1
print(cnt)

