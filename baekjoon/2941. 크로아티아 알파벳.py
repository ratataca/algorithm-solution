alphabet = input()
target = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

alphabets = list(alphabet)

cnt = 0
for t in target:
    while True:
        if t in alphabet:
            si = alphabet.find(t)
            ei = si + len(t)

            for i in range(si, ei):
                alphabets[i] = "0"

            cnt += 1
            alphabet = "".join(alphabets)
        else:
            break

for i in alphabet:
    if i != "0":
        cnt += 1

print(cnt)
