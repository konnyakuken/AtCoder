N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
nums=list()

for i in range(max(N,M)):
    if(i <= min(N,M)-1):
        if(N <= M):
            nums.append([B[i],"B"])
            nums.append([A[i],"A"])
        else:
            nums.append([A[i],"A"])
            nums.append([B[i],"B"])
    else:
        if(M <= N):
            nums.append([A[i],"A"])
        else:
            nums.append([B[i],"B"])

nums.sort(reverse=False, key=lambda x:x[0])

diff = abs(A[0] - B[0])

for i in range((N+M)-1):
    if(nums[i][1] != nums[i+1][1]):
        now_diff = abs(nums[i][0] - nums[i+1][0])
        if(now_diff<=diff):
            diff = now_diff
            if(diff == 0):
                print(diff)
                exit()

print(diff)
    

