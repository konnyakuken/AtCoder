H,W,X,Y=map(int,input().split())
S=[]
for i in range(H):
    s=list(input())
    S.append(s)
print(S)
count=0


for i in range(W):#横の処理
    if(Y-i<0):
        break
    elif(S[X-1][Y-i]=="#"):
        break
    elif(S[X-1][Y-i]=="."):
        count+=1

for i in range(W):
    if(Y+i>=W):
        break
    elif(S[X-1][Y+i]=="#"):
        break
    elif(S[X-1][Y+i]=="."):
        count+=1
count-=1#重複を削除

for i in range(H):#タテの処理
    if(X-i<0):
        break
    elif(S[X-i][Y-1]=="#"):
        break
    elif(S[X-i][Y-1]=="."):
        count+=1

for i in range(H):
    if(X+i>=H):
        break
    elif(S[X+i][Y-1]=="#"):
        break
    elif(S[X+i][Y-1]=="."):
        count+=1
count-=1#重複を削除
print(count)
