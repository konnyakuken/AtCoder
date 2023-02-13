N = int(input())

#これは同じ要素の繰り返しなので一つを変えると全部変わる
#dp =[[0]*3]*N
dp = [[0,0,0] for i in range(N)]
a,b,c = map(int,input().split())
dp[0][0] = a
dp[0][1] = b
dp[0][2] = c
if N == 1:
    print(max(a,b,c))
    exit()
else:
    for i in range(1,N):
        a,b,c = map(int,input().split())
        a1 = dp[i-1][1] + a
        a2 = dp[i-1][2] + a
        b1 = dp[i-1][0] + b
        b2 = dp[i-1][2] + b
        c1 = dp[i-1][0] + c
        c2 = dp[i-1][1] + c
        dp[i][0] = max(a1,a2)
        dp[i][1] = max(b1,b2)
        dp[i][2] = max(c1,c2)

print(max(dp[N-1]))
    