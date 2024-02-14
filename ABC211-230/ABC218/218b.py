P = list(map(int,input().split()))
ans = list()
for i in P:
    ans.append(chr(i+96))
print("".join(ans))