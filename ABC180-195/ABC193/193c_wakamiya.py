N=int(input())
count=0
sq=int(N**0.5)
for i in range(2,sq+1):
    for j in range(2,N+1):
        a=i**j
        if a <=N:
            count+=1
        if a>N:
            break
ans = N-count
print(ans)        