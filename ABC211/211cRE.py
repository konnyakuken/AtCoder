S = input()
N = len(S)

dp = [[0]*N]*8


for i in range(N):
    if(i == 0):
        if S[i] == "c":
            pass

    if S[i] == "c":
        dp[0][i] += 1
        


print(dp)