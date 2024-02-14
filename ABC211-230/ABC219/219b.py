S = list()
ans = ""
for i in range(3):
    S.append(input())
num = input()

for i in num:
    ans += S[int(i)-1]

print(ans)