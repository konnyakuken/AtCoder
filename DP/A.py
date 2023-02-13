N = int(input())
h = list(map(int,input().split()))

dp = [0]*N
#最初に0を除くと 1 2 1 3 1とかのケースがおかしくなる(コーナーケース)
flag = [False]*N

for i in range(N -1):
    #out of rangeにならないように例外処理
    if(i != N-2 ):

        if flag[i+1] == True:
            dp[i+1] = min(dp[i+1],dp[i]+abs(h[i]-h[i+1]))
        else:
            flag[i+1] = True
            if(i == 0):
                dp[i+1] = dp[i]+ abs(h[0]-h[i+1])
            else:
                dp[i+1] = dp[i]+ abs(h[i]-h[i+1])
        
        if flag[i+2] == True:
            dp[i+2] = min(dp[i+2],dp[i]+abs(h[i]-h[i+2]))
        else:
            flag[i+2] = True
            if(i == 0):
                dp[i+2] = dp[i]+ abs(h[0]-h[i+2])
            else:
                dp[i+2] = dp[i]+abs(h[i]-h[i+2])
    else:
        if flag[i+1] == True:
            dp[i+1] = min(dp[i+1],dp[i]+abs(h[i]-h[i+1]))
        else:
            dp[i+1] = dp[i]+ abs(h[i]-h[i+1])



print(dp[N-1])


    




