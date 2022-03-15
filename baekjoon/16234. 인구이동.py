
N, L, R = 3, 5, 10
# N, L, R = [int(n) for n in input().split()]

area = []

# area.append([1000] * (N+1))
# for _ in range(N):
#     area.append([1000] + [int(n) for n in input().split()])


area = [[1000, 1000, 1000, 1000], [1000, 10, 15, 20], [1000, 20, 30, 25], [1000, 40, 22, 10]]
day = 0

print(area)

DX = [0, 0, -1, 1]
DY = [-1, 1, 0, 0]

while True:
    change_idx = set()
    nums = 0
    flag = False
    for y in range(1, N+1):
        for x in range(1, N+1): 
            target = area[y][x]

            if y != N and \
                (L <= abs(target - area[y-1][x]) <= R \
                or L <= abs(target - area[y][x-1]) <= R \
                or L <= abs(target - area[y][x+1]) <= R \
                or L <= abs(target - area[y+1][x]) <= R):
                nums += target
                change_idx.add((x, y))
                flag = True

            elif y == N  and x != N\
                and (L <= abs(target - area[y-1][x]) <= R \
                or L <= abs(target - area[y][x-1]) <= R \
                or L <= abs(target - area[y][x+1]) <= R):

                nums += target
                change_idx.add((x, y))
                flag = True
            elif y == N and x == N\
                and (L <= abs(target - area[y-1][x]) <= R \
                or L <= abs(target - area[y][x-1]) <= R):
                nums += target
                change_idx.add((x, y))
                flag = True
            
            # for dx, dy in zip(DX, DY):
            #     nx, ny = x + dx, y + dy

            #     if 0 < nx < N and 0 < ny < N:
            #         nums += target
            #         change_idx.add((nx, ny))
            #         flag = True

            #     elif 0 < nx < N and ny != 0:
            #         nums += target
            #         change_idx.add((nx, ny))
            #         flag = True

            #     elif nx != 0 and 0 < ny < N:
            #         nums += target
            #         change_idx.add((nx, ny))
            #         flag = True


            

    if flag == False:
        break
    else:
        avg = int(nums / len(change_idx))
        for x, y in change_idx:
            area[y][x] = avg
            
    print(day)

print(day)