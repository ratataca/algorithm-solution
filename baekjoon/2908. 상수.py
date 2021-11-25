# Sol) 1
arr = [n for n in input().split()]
new_arr = []

for a in arr:
    new_text = ""
    for i in range(2, -1, -1):
        new_text += a[i]
    new_arr.append(int(new_text))

print(max(new_arr))

# Sol) 2
# print(max([int(text[::-1]) for text in input().split(" ")]))

# Sol) 3
# arr = [n for n in input().split(" ")]
#
# for i in range(len(arr)):
#     text = list(arr[i])
#
#     text[0], text[2] = text[2], text[0]
#
#     arr[i] = int("".join(text))
#
# print(max(arr))