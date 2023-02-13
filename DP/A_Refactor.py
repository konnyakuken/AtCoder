N= int(input())
h = list(map(int,input().split()))

dp = [0]*N
#最初に0を除くと 1 2 1 3 1とかのケースがおかしくなる(コーナーケース)
flag = [False]*N

for i in range(N -1):
    #out of rangeにならないように例外処理
    for j in range(2):
        j += 1
        if (i + j <= N-1):
            if flag[i+j] == True:
                dp[i+j] = min(dp[i+j],dp[i]+abs(h[i]-h[i+j]))
            else:
                flag[i+j] = True
                if(i == 0):
                    dp[i+j] = dp[i]+ abs(h[0]-h[i+j])
                else:
                    dp[i+j] = dp[i]+ abs(h[i]-h[i+j])


print(dp[N-1])

    




