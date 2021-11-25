T = int(input())
words = []
for i in range(T):
    words.append(input())
cnt = 0


for word in words:
    char_dict = set()
    previous_char = ""
    is_group_word = True

    for w in word:
        if w in char_dict and previous_char != w:
            is_group_word = False
            break

        previous_char = w
        char_dict.add(w)

    if is_group_word:
        cnt += 1

print(cnt)