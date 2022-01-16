from collections import defaultdict

n = int(input())
data = []
for i in range(n):
    data.append(int(input()))

data = sorted(data)

# 1
avg = int(sum(data)/len(data) + 0.5)

# 2
mid = data[len(data) // 2]

# 3
cnt_dict = defaultdict(int)
for i in data:
    cnt_dict[i] =+ 1

cnt_sort = sorted(cnt_dict.items(), key= lambda x : x[1])

if len(cnt_sort) > 1 and cnt_sort[0][1] == cnt_sort[1][1]:
    cnt =  cnt_sort[1][0]
else:
    cnt = cnt_sort[0][0]
# 4
diff = data[-1] - data[0]

print(avg)
print(mid)
print(cnt)
print(diff)