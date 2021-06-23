import itertools
N,M,k=map(int,input().split())
n=list()
for i in range(M):
    A=tuple(map(int,input().split()))
    n.append(A)
ans=list()
for i in range(N):
    for pair in itertools.combinations(n[i], 2):
        ans.append(pair)
tmp = [x for x in set(ans) if ans.count(x) >= k]
print(len(tmp))
