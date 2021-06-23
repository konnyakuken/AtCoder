import itertools
N,M,k=map(int,input().split())
n=list()
for i in range(M):
    A=list(map(int,input().split()))
    n.append(A)
ans=list()
for i in range(N):
    for pair in itertools.combinations(n[i], 2):
        ans.append(pair)
ans.sort()
ans_count=0
count=0
before=0
for i in ans:
    if i==before:
        count+=1
    else:
        if count>=k:
            ans_count+=1
        count=1
    before=i
print(ans_count)