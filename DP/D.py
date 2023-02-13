N,W = map(int,input().split())

item = list()
for i in range(N):
    w,v = map(int,input().split())
    item.append([w,v])
dp = [[0]*(W+1) for i in range(N+1)]
#print(item)

for n in range(N):
    for w in range(W+1):
        if(w >= item[n][0]):
            dp[n+1][w] = max(dp[n][w-item[n][0]] + item[n][1], dp[n][w])
        else:
             dp[n+1][w] = dp[n][w]


print(dp[N][W])

