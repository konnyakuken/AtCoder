N=int(input())
count=0
for i in reversed(range(N)):
    for j in range(N):
        i
    a=i**j
    if a <=N:
        count+=1
    if a>N:
        break
ans = N-count
print(ans)        