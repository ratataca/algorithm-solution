M = int(input())
alphabet = [input() for _ in range(M)]

alphabet = sorted(set(alphabet), key=lambda x : (len(x), x))

for alph in alphabet:
    print(alph)