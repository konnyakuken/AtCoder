import itertools
N,M,k=map(int,input().split())
n = [tuple(map(int,input().split())) for _ in range(M)]
ans=list()
for i in range(N):
    for pair in itertools.combinations(n[i], 2):
        ans.append(pair)
tmp = [x for x in set(ans) if ans.count(x) >= k]
print(len(tmp))
