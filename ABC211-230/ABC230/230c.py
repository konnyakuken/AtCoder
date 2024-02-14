N,A,B = map(int,input().split())
P,Q,R,S = map(int,input().split())
k_11 = max(1-A,1-B)
k_12 = min(N-A,N-B)
k_21 = max(1-A,B-N)
k_22 = min(N-A,B-1)
output = Q-P+1
plot = []
#print(k_11,k_12,k_21,k_22,output)
nowCount = P

for i in range(output):
   plotlist = ["."]*(S-R+1)
   if(k_11 <= (nowCount - A) <= k_12):
      if(R <= B+(nowCount-A) <= S):
        nowJ = B+(nowCount-A)
        #print(nowCount,nowJ)
        plotlist[nowJ-R] = "#"
   if(k_21 <= (nowCount - A) <= k_22):
      if(R <= B-(nowCount-A) <= S):
        nowJ = B-(nowCount-A)
        #print(nowCount,B-(nowCount-A))
        plotlist[nowJ-R] = "#"
   print("".join(plotlist))   
   nowCount += 1