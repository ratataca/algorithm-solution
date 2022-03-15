num = [int(n) for n in input().split()]

ascending = [1, 2, 3, 4, 5, 6, 7, 8]
descending = [8, 7, 6, 5, 4, 3, 2, 1]

if num == ascending:
    print('ascending')
elif num == descending:
    print('descending')
else:
    print('mixed')