N,K = map(int,input().split())

sum = 0

for i in range(N):
    for j in range(K):
        sum += (i+1)*100+(j+1)

print(sum)