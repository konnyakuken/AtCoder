S = input()
N = len(S)
ans = list()
if(N == 1):
    print(S)
    print(S)
    exit()

for i in range(N):
    S = S[1:N]+S[0]
    ans.append(S)
ans.sort()

print(ans[0])
print(ans[-1])