N = int(input())
A = list(map(int,input().split()))
ans = list()
for i in range(N):
    ans.append([A[i],i+1])
ans.sort(reverse=False, key=lambda x:x[0])
print(ans[-2][1])