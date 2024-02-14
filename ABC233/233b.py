L,R = map(int,input().split())
S = input()
S_length = len(S)
ans =""
for i in range(L-1):
    ans += S[i]
for i in reversed(range(L-1,R)):
    ans += S[i]
for i in range(R,S_length):
    ans += S[i]
print(ans)

