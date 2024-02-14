ans = ["ABC","ARC","AGC","AHC"]
S = list()
for i in range(3):
    S.append(input())
print(list(set(ans) ^ set(S))[0])