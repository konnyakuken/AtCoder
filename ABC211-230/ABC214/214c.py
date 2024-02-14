N = int(input())
S = list(map(int,input().split()))
T = list(map(int,input().split()))
ans = T[0]
ans_list= [T[0]]
for i in range(1,N):
    ans = min(T[i],ans+S[i-1])
    ans_list.append(ans)
for i in range(N):
    ans = min(T[i],ans+S[i-1])
    ans_list[i] = ans
#if (min(T[0],ans+S[N-1])!=T[0]):
#    ans_list[0] = ans+S[N-1]

for i in ans_list:
    print(i)

